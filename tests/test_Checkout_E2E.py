from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_e2e(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1. Login
    login_page.abrir()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert "/inventory.html" in driver.current_url

    # 2. Inventario
    nombre_producto = (
        inventory_page.obtener_nombre_primer_producto()
    )

    print(f"Producto seleccionado: {nombre_producto}")

    inventory_page.agregar_primer_producto_al_carrito()

    assert cart_page.obtener_contador_carrito() == "1"

    # 3. Carrito
    cart_page.abrir_carrito()

    assert "/cart.html" in driver.current_url

    nombres_carrito = cart_page.obtener_nombres_productos()

    assert nombre_producto in nombres_carrito

    # 4. Checkout
    checkout_page.iniciar_checkout()

    assert "/checkout-step-one.html" in driver.current_url

    # 5. Datos
    checkout_page.completar_datos(
        "Yndira",
        "Ramirez",
        "1824"
    )

    # 6. Resumen
    checkout_page.continuar()

    assert "/checkout-step-two.html" in driver.current_url

    producto_resumen = (
        checkout_page.obtener_nombre_producto_resumen()
    )

    assert producto_resumen == nombre_producto

    # 7. Finalizar
    checkout_page.finalizar_compra()

    assert "/checkout-complete.html" in driver.current_url

    # 8. Confirmación
    mensaje = (
        checkout_page.obtener_mensaje_confirmacion()
    )

    assert mensaje == "Thank you for your order!"

    print("Checkout realizado correctamente")
    print(f"Producto comprado: {nombre_producto}")