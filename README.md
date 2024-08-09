# Comparador de Tabelas entre Bases Multi Servidores
## Descrição
Este projeto é um comparador de tabelas entre bases de dados que estão distribuídas em múltiplos servidores. Ele permite identificar diferenças entre estruturas de tabelas (colunas, tipos de dados, etc.) e dados armazenados, facilitando a sincronização e manutenção de consistência entre diferentes ambientes de banco de dados.

## Funcionalidades
- Comparação de estrutura de tabelas entre bases de dados em diferentes servidores.
- Identificação de colunas ausentes, tipos de dados inconsistentes, e outras discrepâncias estruturais.
- Comparação de dados entre tabelas, destacando registros diferentes ou ausentes.
- Geração de relatórios detalhados das diferenças encontradas.

## Requisitos
- Linguagem: [Nome da linguagem usada, ex: Python 3.8+]
- Bibliotecas:
  - pandas
  - sqlalchemy
  - pyodbc
 
# Após aparecer os processos concluídos, ao verificar onde o arquivo compare.py foi instalado, também há 2 arquivos .csv
-	diff_prd_to_hml
    -	Esse arquivo é responsável por trazer todas as regras que existem em PRD e não estão no ambiente de HML

- diff_hml_to_prd
  - Esse arquivo é responsável por trazer todas as regras que existem em HML e não estão no ambiente de HML
