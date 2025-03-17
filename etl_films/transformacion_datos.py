import pandas as pd
import pandas.api.types as ptypes
import logging
import os

log_file = os.path.join("Logs", "etl_films.log")
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def transform_data(dataframes):
    logging.info("Iniciando la transformación de datos.")
    transformed_data = {}
    
    try: 
        for sheet_name, df in dataframes.items():
            logging.info(f"Transformando datos de la hoja: {sheet_name}")

            df.columns = [col.lower().lstrip() for col in df.columns]

            df = df.drop_duplicates()

            for col in df.columns:
                df.loc[:, col] = df[col].replace(' NULL', None)

                if ptypes.is_string_dtype(df[col]):
                    df.loc[:, col] = df[col].astype(str).str.strip()

                if (col == 'release_year' or col == 'rental_rate' or col =='replacement_cost'
                    or col =='length' or col == 'film_id' or col =='store_id'):
                    df.loc[:, col] = pd.to_numeric(df[col].astype(str).str.replace(r'[^\d.]+', '', regex=True), errors='coerce')

                if col == 'first_name' or col == 'last_name':
                    df.loc[:, col] = df[col].apply(lambda x: str(x).capitalize())

                logging.info(f"Datos de la columna '{col}' transformados correctamente.")
            transformed_data[sheet_name] = df

        logging.info("Transformación de datos completada.")
        return transformed_data
    
    except Exception as e:
        logging.error(f"La transformación de datos a fallado: {e}")