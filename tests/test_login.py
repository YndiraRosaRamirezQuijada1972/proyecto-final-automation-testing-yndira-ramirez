from pages.login_page import LoginPage


def test_login_exitoso(driver):

    login_page = LoginPage(driver)

    login_page.abrir()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert "/inventory.html" in driver.current_url

    assert driver.title == "Swag Labs" # Cambiamos el título "Swag Labs" por "Titulo incorrecto" para verificar que se crea la captura porque falla
         
