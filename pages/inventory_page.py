from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    PRODUCTOS = (By.CLASS_NAME, "inventory_item")
    NOMBRE_PRODUCTO = (By.CLASS_NAME, "inventory_item_name")
    PRECIO_PRODUCTO = (By.CLASS_NAME, "inventory_item_price")
    MENU = (By.ID, "react-burger-menu-btn")
    FILTRO = (By.CLASS_NAME, "product_sort_container")
    BOTON_AGREGAR = (By.CSS_SELECTOR, ".inventory_item button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_productos(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCTOS)
        )

    def obtener_primer_producto(self):
        productos = self.obtener_productos()
        return productos[0]

    def obtener_nombre_primer_producto(self):
        primer_producto = self.obtener_primer_producto()

        return primer_producto.find_element(
            By.CLASS_NAME,
            "inventory_item_name"
        ).text

    def obtener_precio_primer_producto(self):
        primer_producto = self.obtener_primer_producto()

        return primer_producto.find_element(
            By.CLASS_NAME,
            "inventory_item_price"
        ).text

    def menu_esta_visible(self):
        menu = self.wait.until(
            EC.visibility_of_element_located(self.MENU)
        )
        return menu.is_displayed()

    def filtro_esta_visible(self):
        filtro = self.wait.until(
            EC.visibility_of_element_located(self.FILTRO)
        )
        return filtro.is_displayed()

    def agregar_primer_producto_al_carrito(self):
        boton = self.wait.until(
        EC.element_to_be_clickable(
            self.BOTON_AGREGAR
        )
    )
        boton.click()