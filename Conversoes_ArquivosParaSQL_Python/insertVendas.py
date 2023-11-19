import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

df = pd.read_csv('C:\\Nova pasta\\FatoDetalhes_DadosModelagem.csv', delimiter=';')

numeric_columns = ['Valor', 'Desconto', 'Custo', 'ValorLiquido']

#PostgresSQL utiliza . como separador decimal nos campos do tipo numeric
df[numeric_columns] = df[numeric_columns].apply(lambda x: x.str.replace(',', '.'))

#Colunas com UPPER do CSV precisam ser convertidas para lower para o insert
df.columns = df.columns.str.lower()

df.to_sql('tbvenda', con=engine, schema='public', if_exists='append', index=False)

engine.dispose()