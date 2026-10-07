from selenium.webdriver.common.by import By
 
from utils.helpers import crear_driver, realizar_login
 
 
def test_inventory():
 
    driver = crear_driver()
    
    try:
        realizar_login(driver)
        
        # Validar que nos encontramos en el inventario
        assert "/inventory.html" in driver.current_url
        
        # Validar el título del navegador
        assert driver.title == "Swag Labs"
        
        # Obtener todos los productos
        productos = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item"
        )
        
        # Validar que exista al menos un producto
        assert len(productos) > 0
        
        # Obtener el primer producto
        primer_producto = productos[0]
        
        nombre = primer_producto.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
        ).text
        
        precio = primer_producto.find_element(
        By.CLASS_NAME,
        "inventory_item_price"
        ).text
        
        # Mostrar nombre y precio en consola
        print(f"Primer producto: {nombre}")
        print(f"Precio: {precio}")
        
        # Validar que nombre y precio tengan contenido
        assert nombre != ""
        assert precio != ""
        
        # Validar elementos importantes de la interfaz
        menu = driver.find_element(
        By.ID,
        "react-burger-menu-btn"
        )
        
        filtro = driver.find_element(
        By.CLASS_NAME,
        "product_sort_container"
        )
        
        assert menu.is_displayed()
        assert filtro.is_displayed()
 
    finally:
        driver.quit()
