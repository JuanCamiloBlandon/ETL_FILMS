from .configuración_bd import get_connection
import logging
import os

log_file = os.path.join("Logs", "etl_films.log")
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data_to_mysql(dataframes):
    connection = get_connection()
    if connection:
        cursor = connection.cursor()

        orden_carga = ['store', 'customer', 'film', 'inventory', 'rental']
        for sheet_name in orden_carga:
            if sheet_name in dataframes:
                df = dataframes[sheet_name]
                try:
                    logging.info(f"Cargando datos en la tabla: {sheet_name}")

                    if(sheet_name == 'film'):
                        df = df.drop('num_voted_users', axis=1)

                    if(sheet_name == 'customer'):
                        df = df.drop(['customer_id_old', 'segment'], axis=1)

                    print(f"Nombre de la tabla: {sheet_name}")
                    print(f"Número de columnas: {len(df.columns)}")
                    print(f"Nombres de las columnas: {df.columns.tolist()}")

                    for _, row in df.iterrows():
                        placeholders = ", ".join(["%s"] * len(df.columns))
                        insert_query = f"INSERT INTO {sheet_name} VALUES ({placeholders})"
                        #print(row)
                        cursor.execute(insert_query, tuple(row))

                    connection.commit()
                    logging.info(f"Datos de la tabla '{sheet_name}' cargados con éxito.")
                    print(f"Datos de la tabla '{sheet_name}' cargados con éxito.")
                except Exception as e:
                    print(f"Error al cargar datos de la tabla '{sheet_name}': {e}")
                    logging.error(f"Error al cargar datos de la tabla '{sheet_name}': {e}")
                    connection.rollback()
            else:
                print(f"Advertencia: DataFrame '{sheet_name}' no encontrado.")
                logging.warning(f"Advertencia: DataFrame '{sheet_name}' no encontrado.")
        connection.close()
    else:
        print("No se pudo establecer la conexión a la base de datos.")
        logging.error("No se pudo establecer la conexión a la base de datos.")