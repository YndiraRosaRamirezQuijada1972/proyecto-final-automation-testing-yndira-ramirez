from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class CartPage:

    # Localizadores
    CARRITO = (By.CLASS_NAME, "shopping_cart_link")
    CONTADOR_CARRITO = (By.CLASS_NAME, "shopping_cart_badge")
    PRODUCTOS_CARRITO = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_contador_carrito(self):
        contador = self.wait.until(
            EC.visibility_of_element_located(
                self.CONTADOR_CARRITO
            )
        )
        return contador.text

    def abrir_carrito(self):
        carrito = self.wait.until(
            EC.element_to_be_clickable(
                self.CARRITO
            )
        )
        carrito.click()

        self.wait.until(
            EC.url_contains("/cart.html")
        )

    def obtener_nombres_productos(self):

        def obtener_textos(driver):
            try:
                productos = driver.find_elements(
                    *self.PRODUCTOS_CARRITO
                )

                nombres = [
                    producto.text
                    for producto in productos
                    if producto.is_displayed()
                ]

                return nombres if nombres else False

            except StaleElementReferenceException:
                return False

        return self.wait.until(obtener_textos)