import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

df = pd.read_csv('C:\\Nova pasta\\FatoCabecalho_DadosModelagem.txt', sep='\t')

numeric_columns = ['ValorFrete']

#PostgresSQL utiliza . como separador decimal nos campos do tipo numeric
df[numeric_columns] = df[numeric_columns].apply(lambda x: x.str.replace(',', '.'))

df.columns = df.columns.str.lower()

df.to_sql('tbfrete', con=engine, schema='public', if_exists='append', index=False)

engine.dispose()