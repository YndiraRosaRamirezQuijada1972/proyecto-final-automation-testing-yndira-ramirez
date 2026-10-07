from utils.helpers import crear_driver, realizar_login
 
 
def test_login_exitoso():
 
    driver = crear_driver()
    
    try:
        realizar_login(driver)
        
        # Validar que la URL sea la correspondiente al inventario
        assert "/inventory.html" in driver.current_url
        
        # Validar el título de la página
        assert driver.title == "Swag Labs"
 
    finally:
        driver.quit()
