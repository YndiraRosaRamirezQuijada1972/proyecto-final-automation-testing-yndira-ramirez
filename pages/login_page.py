from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    URL = "https://www.saucedemo.com/"

    # Localizadores
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self):
        self.driver.get(self.URL)

    def ingresar_usuario(self, username):
        usuario = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        )
        usuario.send_keys(username)

    def ingresar_password(self, password):
        clave = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        )
        clave.send_keys(password)

    def hacer_click_login(self):
        boton = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        boton.click()

    def login(self, username, password):
        self.ingresar_usuario(username)
        self.ingresar_password(password)
        self.hacer_click_login()

    def obtener_mensaje_error(self):
        mensaje = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return mensaje.text