from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
from utils.helpers import crear_driver, realizar_login
 
 
def test_agregar_producto_al_carrito():
 
    driver = crear_driver()
    
    try:
        realizar_login(driver)
        
        wait = WebDriverWait(driver, 10)
        
        # Esperar hasta que aparezcan los productos
        wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "inventory_item")
            )
        )
        
        # Obtener el nombre del primer producto
        nombre_producto = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        ).text
        
        print(f"Producto seleccionado: {nombre_producto}")
        
        # Buscar nuevamente el botón justo antes de hacer clic
        boton_agregar = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".inventory_item button")
            )
        )
        
        boton_agregar.click()
        
        # Esperar hasta que aparezca el contador del carrito
        contador = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "shopping_cart_badge")
            )
        )
        
        assert contador.text == "1"
        
        print(f"Cantidad en carrito: {contador.text}")
        
        # Buscar el carrito y hacer clic
        carrito = wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        )
        
        carrito.click()
        
        # Esperar hasta llegar al carrito
        wait.until(
            EC.url_contains("/cart.html")
        )
        
        # Obtener nuevamente los productos
        productos_carrito = wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        )
    finally:
        driver.quit()
