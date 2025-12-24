import pandas as pd

def create_dim_products(df):
    """Cria a dimensão de produtos."""
    dim_products = df[['product_name']].drop_duplicates().reset_index(drop=True)
    dim_products['product_id'] = dim_products.index + 1
    
    # Adicionando categoria fictícia baseada no nome (exemplo simples)
    categories_map = {
        'Laptop': 'Eletrônicos', 'Mouse': 'Acessórios', 'Teclado': 'Acessórios',
        'Monitor': 'Eletrônicos', 'Headset': 'Áudio', 'Webcam': 'Vídeo'
    }
    dim_products['category'] = dim_products['product_name'].map(categories_map)
    return dim_products[['product_id', 'product_name', 'category']]

def create_dim_customers(df):
    """Cria a dimensão de clientes."""
    dim_customers = df[['customer_id']].drop_duplicates().reset_index(drop=True)
    # Simulando nomes de clientes
    dim_customers['customer_name'] = "Cliente " + dim_customers['customer_id'].astype(str)
    return dim_customers

def create_dim_date(df):
    """Cria a dimensão de tempo."""
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    dates = pd.DataFrame({'date': df['transaction_date'].unique()})
    dates['date_id'] = dates['date'].dt.strftime('%Y%m%d').astype(int)
    dates['day'] = dates['date'].dt.day
    dates['month'] = dates['date'].dt.month
    dates['year'] = dates['date'].dt.year
    dates['quarter'] = dates['date'].dt.quarter
    dates['day_of_week'] = dates['date'].dt.dayofweek
    return dates

def create_fact_sales(df, dim_products, dim_date):
    """Cria a tabela fato de vendas."""
    fact_sales = df.copy()
    fact_sales['transaction_date'] = pd.to_datetime(fact_sales['transaction_date'])
    
    # Join com dimensões para obter IDs
    fact_sales = fact_sales.merge(dim_products, on='product_name')
    fact_sales['date_id'] = fact_sales['transaction_date'].dt.strftime('%Y%m%d').astype(int)
    
    # Selecionando colunas da fato
    fact_columns = [
        'transaction_id', 'product_id', 'customer_id', 'date_id',
        'quantity', 'unit_price', 'total_amount', 'store_location'
    ]
    return fact_sales[fact_columns]

def run_transform(input_path):
    """Executa as transformações e retorna os dataframes dimensionais."""
    print("Iniciando transformações (Modelagem Dimensional)...")
    df = pd.read_csv(input_path)
    
    dim_products = create_dim_products(df)
    dim_customers = create_dim_customers(df)
    dim_date = create_dim_date(df)
    fact_sales = create_fact_sales(df, dim_products, dim_date)
    
    print("Transformações concluídas com sucesso.")
    return {
        'dim_products': dim_products,
        'dim_customers': dim_customers,
        'dim_date': dim_date,
        'fact_sales': fact_sales
    }
