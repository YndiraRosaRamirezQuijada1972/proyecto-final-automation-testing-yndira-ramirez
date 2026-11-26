Proyecto Final - Framework de Automatización de Pruebas
Proyecto final de automatización de pruebas desarrollado con Python, Selenium WebDriver y Pytest.

El framework incluye pruebas automatizadas sobre la aplicación web SauceDemo, pruebas de API, implementación del patrón Page Object Model (POM), datos externos en JSON, generación de reportes HTML, captura automática de screenshots ante fallos y registro de ejecución mediante logging.

Objetivo
Desarrollar un framework de automatización que permita ejecutar y mantener pruebas funcionales de manera organizada, reutilizable y escalable.

El proyecto implementa:
Automatización Web con Selenium WebDriver.
Pytest como framework de ejecución.
Page Object Model (POM).
Pruebas de API utilizando Requests.
Datos de prueba externos mediante JSON.
Parametrización de escenarios.
Fixtures de Pytest.
Screenshots automáticos ante fallos.
Reporte HTML de resultados.
Logging de ejecución.


Tecnologías utilizadas
Python 3
Selenium WebDriver
Pytest
Pytest HTML
Requests
Google Chrome
Visual Studio Code
Git
GitHub


Estructura del proyecto
proyecto-final-automation-testing-yndira-ramirez/
│
├── data/
│   └── users.json
│
├── logs/
│   └── automation.log
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── reports/
│   └── report.html
│
├── screenshots/
│
├── tests/
│   ├── api/
│   │   └── test_api.py
│   │
│   ├── test_Checkout_E2E.py
│   ├── test_cart.py
│   ├── test_inventory.py
│   ├── test_login.py
│   └── test_login_invalido.py
│
├── utils/
│   ├── helpers.py
│   └── logger.py
│
├── .gitignore
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md


Page Object Model (POM)
El proyecto utiliza el patrón Page Object Model para separar la lógica de interacción con las páginas de los casos de prueba.

Los Page Objects se encuentran en la carpeta: pages/

Se implementaron:
login_page.py
inventory_page.py
cart_page.py
checkout_page.py
Esto permite centralizar localizadores y acciones, evitando duplicación de código dentro de los tests.



Pruebas automatizadas
Actualmente la suite contiene 9 pruebas automatizadas.


Pruebas Web
Login exitoso
Valida que un usuario válido pueda iniciar sesión correctamente en SauceDemo.

Login inválido
Valida distintos escenarios de credenciales inválidas utilizando parametrización y datos externos.

Inventory
Valida información de los productos disponibles en el inventario.

Carrito
Valida que un producto pueda agregarse correctamente al carrito.

Checkout E2E
Valida el flujo End-to-End desde el inicio de sesión hasta la finalización del proceso de compra.



Pruebas de API
El proyecto incluye pruebas de API utilizando la librería requests.

Se validan operaciones como:
GET
POST
DELETE
Las pruebas se encuentran en: tests/api/test_api.py



Datos externos
Los datos utilizados por determinados escenarios se encuentran separados del código de prueba.

Archivo:
data/users.json
Esto permite reutilizar los datos y facilita el mantenimiento de los casos de prueba.



Fixtures
El archivo: conftest.py
centraliza configuraciones compartidas por los tests, incluyendo la creación y cierre del navegador.

Esto evita repetir la configuración de Selenium en cada prueba.



Screenshots automáticos
Cuando una prueba Web falla, el framework genera automáticamente una captura de pantalla con evidencia del estado de la aplicación.

Las capturas se almacenan en: screenshots/
El nombre del archivo incluye el nombre del test y la fecha/hora de ejecución.

Las evidencias también pueden incorporarse al reporte HTML generado por Pytest HTML.



Logging
El framework utiliza el módulo logging de Python para registrar información sobre la ejecución de las pruebas.

La configuración se encuentra en: utils/logger.py
Los registros se generan en: logs/automation.log

El log permite registrar eventos como:
Inicio de una prueba.
Finalización de una prueba.
Fallos detectados.
Ubicación de screenshots generados ante errores.



Reporte HTML
Luego de ejecutar la suite se genera automáticamente un reporte en: reports/report.html

El reporte permite consultar:
Tests ejecutados.
Tests exitosos.
Tests fallidos.
Duración de cada prueba.
Detalle de los errores.
Evidencias asociadas a fallos Web.



Instalación
1. Clonar el repositorio
git clone <URL_DEL_REPOSITORIO>
2. Ingresar al proyecto
cd proyecto-final-automation-testing-yndira-ramirez
3. Instalar las dependencias
pip install -r requirements.txt

Las principales dependencias son:
selenium==4.49.0
pytest==9.1.1
pytest-html==4.2.0
requests==2.34.2
Ejecución de las pruebas

Desde la raíz del proyecto ejecutar: python -m pytest -v
Pytest detectará automáticamente las pruebas ubicadas dentro de la carpeta tests.



Resultado actual
Última ejecución completa: 9 passed
La suite completa se ejecuta correctamente.



Resultado de la ejecución
El framework genera como evidencias:
reports/report.html
logs/automation.log
screenshots/
Estas evidencias permiten analizar los resultados y facilitar la detección de errores durante la ejecución automática.



Autora
Yndira Ramirez

Proyecto Final - Automation Testing