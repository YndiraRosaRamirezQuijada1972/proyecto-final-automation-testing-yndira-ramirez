import logging
import os


def get_logger(nombre="automation"):

    # Crear la carpeta logs si no existe
    os.makedirs("logs", exist_ok=True)

    # Crear el logger
    logger = logging.getLogger(nombre)
    logger.setLevel(logging.INFO)

    # Evitar agregar handlers duplicados
    if not logger.handlers:

        # Archivo donde se guardarán los logs
        file_handler = logging.FileHandler(
        "logs/automation.log",
        encoding="utf-8"
        )

        # Formato del log
        formato = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )

        file_handler.setFormatter(formato)

        # Agregar el handler al logger
        logger.addHandler(file_handler)

    return logger
