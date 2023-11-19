import pandas as pd
from sqlalchemy import create_engine


class Insert:
    @staticmethod
    def inserir(self, arquivo, sheetname, tablename):
        engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

        df = pd.read_excel(arquivo, sheet_name=sheetname)

        df.columns = df.columns.str.lower()

        df.to_sql(tablename, con=engine, schema='public', if_exists='append', index=False)

        engine.dispose()
