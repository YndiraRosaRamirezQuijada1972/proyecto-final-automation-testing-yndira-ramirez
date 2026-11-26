from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_inventory(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # Login
    login_page.abrir()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert "/inventory.html" in driver.current_url
    assert driver.title == "Swag Labs"

    # Productos
    productos = inventory_page.obtener_productos()

    assert len(productos) > 0

    nombre = inventory_page.obtener_nombre_primer_producto()
    precio = inventory_page.obtener_precio_primer_producto()

    print(f"Primer producto: {nombre}")
    print(f"Precio: {precio}")

    assert nombre != ""
    assert precio != ""

    # Elementos del inventario
    assert inventory_page.menu_esta_visible()
    assert inventory_page.filtro_esta_visible()