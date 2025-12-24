import sqlite3
import os

def run_load(data_dict, db_path="data/processed/warehouse.db"):
    """Carrega os DataFrames no banco de dados SQLite."""
    print(f"Iniciando carga no Data Warehouse: {db_path}")
    
    # Garantir que o diretório existe
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # Usando sqlite3 nativo para evitar dependências externas no ambiente de execução
    conn = sqlite3.connect(db_path)
    
    for table_name, df in data_dict.items():
        print(f"Carregando tabela: {table_name} ({len(df)} registros)")
        df.to_sql(table_name, conn, if_exists='replace', index=False)
    
    conn.close()
    print("Carga concluída com sucesso.")

if __name__ == "__main__":
    # Apenas para teste individual
    pass
