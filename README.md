# Pre-Entrega - Automatización con Selenium y Pytest
 
Proyecto de automatización de pruebas realizado sobre la aplicación web SauceDemo.
 
## Objetivo
 
Automatizar distintos escenarios funcionales de SauceDemo utilizando Python, Selenium y Pytest.
 
## Tecnologías utilizadas
 
- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- Visual Studio Code
- Google Chrome
 
## Estructura del proyecto
 
```text
Pre_Entrega_Automation_IA/
│
├── tests/
│ ├── __init__.py
│ ├── test_login.py
│ ├── test_inventory.py
│ └── test_cart.py
│
├── utils/
│ ├── __init__.py
│ └── helpers.py
│
├── reports/
│ └── report.html
│
├── pytest.ini
├── requirements.txt
└── README.md
```
 
## Pruebas automatizadas
 
El proyecto contiene tres pruebas automatizadas:
 
### 1. Login
 
Valida el inicio de sesión exitoso en SauceDemo.
 
### 2. Inventory
 
Valida la información del primer producto mostrado en el inventario:
 
- Producto: Sauce Labs Backpack
- Precio: $29.99
 
### 3. Carrito
 
Valida que el producto Sauce Labs Backpack pueda agregarse correctamente al carrito y que el contador del carrito sea igual a 1.
 
## Ejecución de las pruebas
 
Desde la raíz del proyecto ejecutar:
 
```bash
python -m pytest
```
 
Pytest detectará automáticamente las pruebas ubicadas dentro de la carpeta `tests`.
 
## Reporte HTML
 
Luego de ejecutar las pruebas se genera automáticamente un reporte HTML en:
 
```text
reports/report.html
```
 
## Instalación de dependencias
 
Para instalar las dependencias necesarias ejecutar:
 
```bash
pip install -r requirements.txt
```
 
## Resultado actual
 
```text
3 passed
```
 
Las tres pruebas automatizadas se ejecutan correctamente.