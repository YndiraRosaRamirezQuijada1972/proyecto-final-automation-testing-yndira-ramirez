import json
from pathlib import Path

import pytest

from pages.login_page import LoginPage


# Ruta del archivo JSON con los datos de prueba
RUTA_DATOS = Path(__file__).parent.parent / "data" / "users.json"


# Leer los casos de prueba desde el archivo JSON
with open(RUTA_DATOS, "r", encoding="utf-8") as archivo:
    CASOS_LOGIN = json.load(archivo)


@pytest.mark.parametrize("caso", CASOS_LOGIN)
def test_login_invalido(driver, caso):
       
        # Crear Page Object
        login_page = LoginPage(driver)

        # Abrir SauceDemo
        login_page.abrir()

        # Intentar login con los datos provenientes del JSON
        login_page.login(
            caso["username"],
            caso["password"]
        )

        # Obtener el mensaje mediante LoginPage
        mensaje_error = login_page.obtener_mensaje_error()

        # Validar el mensaje esperado
        assert mensaje_error == caso["expected_error"]

        # Validar que el usuario no ingresó al inventario
        assert "/inventory.html" not in driver.current_url
