import mysql.connector
import logging
import os

log_file = os.path.join("Logs", "etl_films.log")
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "film_database"
}

def get_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        logging.info("Conexión a la BD exitosa")
        return connection
    except mysql.connector.Error as error:
        logging.error(f"Error al conectar a la base de datos MySQL: {error}")
        return None