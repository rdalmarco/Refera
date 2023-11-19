import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

df = pd.read_excel('C:\\Nova pasta\\Dimensoes_DadosModelagem.xlsx')

df.columns = df.columns.str.lower()

df.to_sql('tbcliente', con=engine, schema='public', if_exists='append', index=False)

engine.dispose()