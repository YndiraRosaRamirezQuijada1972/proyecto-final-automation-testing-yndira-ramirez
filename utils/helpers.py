from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
 
BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
 
 
def crear_driver():
    """Crea una nueva instancia del navegador Chrome."""
    
    options = webdriver.ChromeOptions()
    
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    
    options.add_experimental_option("prefs", prefs)
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    
    return driver
    
    
def realizar_login(driver):
    """Realiza el login en SauceDemo utilizando credenciales válidas."""
    
    driver.get(BASE_URL)
    
    wait = WebDriverWait(driver, 10)
    
    usuario = wait.until(
    EC.visibility_of_element_located((By.ID, "user-name"))
    )
    
    usuario.send_keys(USERNAME)
    
    password = driver.find_element(By.ID, "password")
    password.send_keys(PASSWORD)
    
    boton_login = driver.find_element(By.ID, "login-button")
    boton_login.click()
    
    # Espera explícita hasta que se cargue la página de inventario
    wait.until(
    EC.url_contains("/inventory.html")
    )
