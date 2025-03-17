from .extraccion_datos import extract_excel_data
from .transformacion_datos import transform_data
from .carga_datos import load_data_to_mysql
import logging
import os

log_file = os.path.join("Logs", "etl_films.log")
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_etl():
    logging.info("Iniciando el ETL.")
    excel_file = r"C:\Users\jblan\Desktop\Prueba  tecnica Quind\ETL_Films\Archivo_Entrada\Films_2 .xlsx"
    extracted_data = extract_excel_data(excel_file)
    if extracted_data:
        transformed_data = transform_data(extracted_data)
        load_data_to_mysql(transformed_data)
        logging.info("ETL completado con éxito.")
    else:
        logging.error("Error en la extracción de datos. El ETL no se ejecutó.")

if __name__ == "__main__":
    run_etl()