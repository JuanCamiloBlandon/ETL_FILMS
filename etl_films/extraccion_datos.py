import pandas as pd
import logging
import os

log_file = os.path.join("Logs", "etl_films.log")
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def extract_excel_data(filepath):

    try:
        logging.info(f"Extrayendo datos del archivo Excel: {filepath}")
        excel_data = pd.read_excel(filepath, sheet_name=None)
        logging.info("Datos del archivo Excel extraídos correctamente.")
        return excel_data
    except FileNotFoundError:
        logging.error(f"Error: El archivo '{filepath}' no fue encontrado.")
        print(f"Error: El archivo '{filepath}' no fue encontrado.")
        return None
    except Exception as e:
        logging.error(f"Error al leer el archivo Excel: {e}")
        print(f"Error al leer el archivo Excel: {e}")
        return None
