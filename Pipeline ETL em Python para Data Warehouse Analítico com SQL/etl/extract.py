import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def generate_mock_data(n_records=1000):
    """Gera dados transacionais fictícios para simular uma fonte de dados."""
    np.random.seed(42)
    
    start_date = datetime(2023, 1, 1)
    dates = [start_date + timedelta(days=np.random.randint(0, 365)) for _ in range(n_records)]
    
    products = ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Headset', 'Webcam']
    categories = ['Eletrônicos', 'Acessórios', 'Acessórios', 'Eletrônicos', 'Áudio', 'Vídeo']
    prod_cat_map = dict(zip(products, categories))
    
    data = {
        'transaction_id': range(1, n_records + 1),
        'customer_id': np.random.randint(100, 200, n_records),
        'product_name': np.random.choice(products, n_records),
        'quantity': np.random.randint(1, 5, n_records),
        'unit_price': np.random.uniform(50, 2000, n_records).round(2),
        'transaction_date': dates,
        'store_location': np.random.choice(['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba'], n_records)
    }
    
    df = pd.DataFrame(data)
    df['total_amount'] = (df['quantity'] * df['unit_price']).round(2)
    return df

def run_extract(output_path):
    """Executa a extração e salva os dados brutos em CSV."""
    print("Iniciando extração de dados...")
    df = generate_mock_data()
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Extração concluída. Dados salvos em: {output_path}")
    return df

if __name__ == "__main__":
    run_extract("data/raw/transactions.csv")
