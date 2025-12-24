import os
from etl.extract import run_extract
from etl.transform import run_transform
from etl.load import run_load

def main():
    """Orquestrador principal do Pipeline ETL."""
    print("="*50)
    print("PIPELINE ETL - DATA WAREHOUSE ANALÍTICO")
    print("="*50)
    
    # Definição de caminhos
    RAW_DATA_PATH = "data/raw/transactions.csv"
    DB_PATH = "data/processed/warehouse.db"
    
    # 1. Extração
    run_extract(RAW_DATA_PATH)
    
    # 2. Transformação
    transformed_data = run_transform(RAW_DATA_PATH)
    
    # 3. Carga
    run_load(transformed_data, DB_PATH)
    
    print("="*50)
    print("PROCESSO FINALIZADO COM SUCESSO!")
    print("="*50)

if __name__ == "__main__":
    main()
