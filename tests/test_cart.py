from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_agregar_producto_al_carrito(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # Login
    login_page.abrir()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert "/inventory.html" in driver.current_url

    # Obtener producto
    nombre_producto = (
        inventory_page.obtener_nombre_primer_producto()
    )

    print(f"Producto seleccionado: {nombre_producto}")

    # Agregar producto
    inventory_page.agregar_primer_producto_al_carrito()

    # Validar contador
    assert cart_page.obtener_contador_carrito() == "1"

    # Abrir carrito
    cart_page.abrir_carrito()

    assert "/cart.html" in driver.current_url

    # Validar producto
    nombres_carrito = cart_page.obtener_nombres_productos()

    assert nombre_producto in nombres_carrito

    print(
        f"Producto encontrado en carrito: {nombre_producto}"
    )