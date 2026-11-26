from datetime import datetime
from pathlib import Path
import base64

import pytest
import pytest_html

from utils.helpers import crear_driver

from utils.logger import get_logger

logger = get_logger()

@pytest.fixture
def driver(request):
    logger.info(f"Iniciando test: {request.node.name}")

    driver = crear_driver()

    # Permite que el hook acceda al navegador
    request.node.driver = driver

    yield driver

    # El navegador se cierra después de generar el reporte
    driver.quit()

    logger.info(f"Finalizando test: {request.node.name}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        logger.error(f"Test fallido: {item.name}")
        
        driver = getattr(item, "driver", None)

        if driver is not None:
            carpeta_screenshots = Path("screenshots")
            carpeta_screenshots.mkdir(exist_ok=True)

            fecha_hora = datetime.now().strftime(
                "%Y-%m-%d_%H-%M-%S"
            )

            nombre_archivo = (
                f"{item.name}_{fecha_hora}.png"
            )

            ruta = carpeta_screenshots / nombre_archivo

            driver.save_screenshot(str(ruta))

            logger.error(f"Screenshot guardado en: {ruta}")

            print(
                f"\nScreenshot guardado en: {ruta}"
            )

            # Agregar screenshot como evidencia al reporte HTML
            extras = getattr(report, "extras", [])

            with open(ruta, "rb") as imagen:
                imagen_base64 = base64.b64encode(
                    imagen.read()
                ).decode("utf-8")   

            extras.append(
                pytest_html.extras.image(
                    imagen_base64,
                    mime_type="image/png",
                    extension="png",
                    name="Screenshot del fallo"
                )
            )

            report.extras = extras
            