from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    # Localizadores
    BOTON_CHECKOUT = (By.ID, "checkout")
    NOMBRE = (By.ID, "first-name")
    APELLIDO = (By.ID, "last-name")
    CODIGO_POSTAL = (By.ID, "postal-code")
    BOTON_CONTINUAR = (By.ID, "continue")
    PRODUCTO_RESUMEN = (By.CLASS_NAME, "inventory_item_name")
    BOTON_FINALIZAR = (By.ID, "finish")
    MENSAJE_CONFIRMACION = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def iniciar_checkout(self):
        boton = self.wait.until(
            EC.element_to_be_clickable(
                self.BOTON_CHECKOUT
            )
        )
        boton.click()

        self.wait.until(
            EC.url_contains("/checkout-step-one.html")
        )

    def completar_datos(self, nombre, apellido, codigo_postal):
        campo_nombre = self.wait.until(
            EC.visibility_of_element_located(
                self.NOMBRE
            )
        )
        campo_nombre.send_keys(nombre)

        campo_apellido = self.wait.until(
            EC.visibility_of_element_located(
                self.APELLIDO
            )
        )
        campo_apellido.send_keys(apellido)

        campo_codigo_postal = self.wait.until(
            EC.visibility_of_element_located(
                self.CODIGO_POSTAL
            )
        )
        campo_codigo_postal.send_keys(codigo_postal)

    def continuar(self):
        boton = self.wait.until(
            EC.element_to_be_clickable(
                self.BOTON_CONTINUAR
            )
        )
        boton.click()

        self.wait.until(
            EC.url_contains("/checkout-step-two.html")
        )

    def obtener_nombre_producto_resumen(self):
        producto = self.wait.until(
            EC.visibility_of_element_located(
                self.PRODUCTO_RESUMEN
            )
        )
        return producto.text

    def finalizar_compra(self):
        boton = self.wait.until(
            EC.element_to_be_clickable(
                self.BOTON_FINALIZAR
            )
        )
        boton.click()

        self.wait.until(
            EC.url_contains("/checkout-complete.html")
        )

    def obtener_mensaje_confirmacion(self):
        mensaje = self.wait.until(
            EC.visibility_of_element_located(
                self.MENSAJE_CONFIRMACION
            )
        )
        return mensaje.text