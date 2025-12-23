import requests
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine

# ==============================
# CONFIGURAÇÕES
# ==============================
API_URL = "https://api.publicapis.org/entries"
DB_CONNECTION = "sqlite:///etl_database.db"

# ==============================
# EXTRAÇÃO
# ==============================
def extract_data(api_url):
    response = requests.get(api_url)
    response.raise_for_status()
    data = response.json()
    return pd.DataFrame(data["entries"])

# ==============================
# TRANSFORMAÇÃO
# ==============================
def transform_data(df):
    df = df[['API', 'Description', 'Category', 'HTTPS']]
    df['load_date'] = datetime.now()
    return df

# ==============================
# CARGA
# ==============================
def load_data(df, connection_string):
    engine = create_engine(connection_string)
    df.to_sql('public_apis', engine, if_exists='replace', index=False)

# ==============================
# PIPELINE
# ==============================
def run_pipeline():
    df_raw = extract_data(API_URL)
    df_transformed = transform_data(df_raw)
    load_data(df_transformed, DB_CONNECTION)
    print("Pipeline ETL executado com sucesso.")

if __name__ == "__main__":
    run_pipeline()
