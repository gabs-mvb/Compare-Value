import pandas as pd
from sqlalchemy import create_engine
import logging
import urllib.parse

# Configuração básica do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configurações do banco de dados
config = {
    'hml': {
        'driver': 'ODBC Driver 17 for SQL Server',
        'server': 'XXXXXXX',
        'database': 'XXXXXXX',
        'username': 'XXXXXXXX',
        'password': 'XXXXXXXX'
    },
    'prd': {
        'driver': 'ODBC Driver 17 for SQL Server',
        'server': 'XXXXXXX',
        'database': 'XXXXXXX',
        'username': 'XXXXXXX',
        'password': 'XXXXXXX'
    }
}

def create_engine_from_config(config):
    try:
        username = urllib.parse.quote_plus(config['username'])
        password = urllib.parse.quote_plus(config['password'])
        server = urllib.parse.quote_plus(config['server'])
        database = urllib.parse.quote_plus(config['database'])
        driver = urllib.parse.quote_plus(config['driver'])

        connection_string = (
            f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}"
        )
        logging.info('Criando engine com a URL de conexão: %s', connection_string)
        return create_engine(connection_string)
    except Exception as e:
        logging.error('Erro ao criar engine: %s', e)
        raise

def fetch_data(engine, query):
    try:
        logging.info('Executando consulta SQL.')
        df = pd.read_sql(query, engine)
        logging.info('Dados carregados com sucesso.')
        return df
    except Exception as e:
        logging.error('Erro ao executar a consulta: %s', e)
        raise

# Criar engines para os dois bancos de dados
logging.info('Criando engines para os bancos de dados prd e hml')
engine_prd = create_engine_from_config(config['prd'])
engine_hml = create_engine_from_config(config['hml'])

# Consulta SQL
query = """
    SELECT DISTINCT A.ID AS ID_EMISSOR
        ,A.NOME
        ,C.ID AS ID_REGRA
        ,C.NOME
    FROM EMISSORES A WITH (NOLOCK)
    INNER JOIN REGRAS_ASSOCIACOES B WITH (NOLOCK) ON B.ID_EMISSOR = A.ID
    INNER JOIN REGRAS C WITH (NOLOCK) ON C.ID = B.ID_REGRA
    ORDER BY A.NOME
"""

# Buscar dados
logging.info('Buscando dados do banco de dados prd.')
df_prd = fetch_data(engine_prd, query)
logging.info('Buscando dados do banco de dados hml.')
df_hml = fetch_data(engine_hml, query)

# Comparar os DataFrames
logging.info('Comparando DataFrames.')
diff_prd_to_hml = pd.concat([df_prd, df_hml, df_hml]).drop_duplicates(keep=False)
diff_hml_to_prd = pd.concat([df_hml, df_prd, df_prd]).drop_duplicates(keep=False)

# Salvar diferenças em arquivos CSV
logging.info('Salvando diferenças em arquivos CSV.')
diff_prd_to_hml.to_csv('diff_prd_to_hml.csv', index=False)
diff_hml_to_prd.to_csv('diff_hml_to_prd.csv', index=False)

logging.info('Processo concluído com sucesso.')

logging.info('Processo concluído com sucesso.')
