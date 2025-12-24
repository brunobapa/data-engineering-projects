# Pipeline ETL em Python para Data Warehouse Analítico com SQL

Este projeto demonstra a implementação de um pipeline de dados completo, desde a extração de dados brutos até a carga em um **Data Warehouse** modelado em **Star Schema** (Esquema Estrela), focado em análise de performance de vendas.

## 🧠 Contexto do Projeto

O objetivo é simular um cenário real de engenharia de dados onde dados transacionais de vendas são processados para permitir análises estratégicas. O projeto foca em:
- **Modelagem Dimensional**: Separação clara entre tabelas Fato e Dimensão.
- **Qualidade de Dados**: Transformações para garantir integridade e padronização.
- **Escalabilidade**: Estrutura modular de código (Extract, Transform, Load).
- **SQL Analítico**: Consultas prontas para geração de insights de negócio.

## 🏗️ Arquitetura e Estrutura

O fluxo de dados segue a arquitetura clássica de ETL:
1. **Extract**: Simulação de dados transacionais (CSV).
2. **Transform**: Limpeza, normalização e criação do modelo dimensional.
3. **Load**: Carga dos dados processados em um banco de dados relacional (SQLite).

### Estrutura do Repositório
```text
projeto-dw-analitico/
├── data/
│   ├── raw/            # Dados brutos (Transactions)
│   └── processed/      # Banco de Dados (Data Warehouse)
├── sql/
│   ├── create_tables.sql      # DDL para o esquema estrela
│   └── queries_analytics.sql  # Consultas para insights
├── etl/
│   ├── extract.py      # Lógica de extração/geração
│   ├── transform.py    # Modelagem dimensional com Pandas
│   └── load.py         # Carga no banco de dados
├── main.py             # Orquestrador do pipeline
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**: Linguagem principal para o pipeline.
- **Pandas**: Manipulação e transformação de dados.
- **SQLite**: Banco de dados relacional para o Data Warehouse.
- **SQL**: Modelagem e consultas analíticas.

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/brunobapa/data-engineering-projects.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o pipeline:
   ```bash
   python main.py
   ```

## 📊 Modelagem Dimensional (Star Schema)

O Data Warehouse foi estruturado com as seguintes tabelas:
- **fact_sales**: Registros de transações, preços e métricas.
- **dim_products**: Detalhes dos produtos e categorias.
- **dim_customers**: Informações dos clientes.
- **dim_date**: Atributos temporais (dia, mês, ano, trimestre) para análise de séries temporais.

## 📈 Exemplos de Insights Gerados (SQL)

O diretório `sql/` contém consultas para responder perguntas como:
- Qual o faturamento total por categoria de produto?
- Qual a evolução mensal das vendas?
- Quem são os top 5 clientes por volume de compras?
- Qual a performance de vendas por localização de loja?

---
*Projeto desenvolvido para fins de portfólio de Engenharia de Dados.*
