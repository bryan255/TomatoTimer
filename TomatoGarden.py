import pyodbc
import datetime
import pandas as pd

class TomatoGarden:

    def __init__(self, conn_str: str):

        self.conn = pyodbc.connect(conn_str)
        self.cursor = self.conn.cursor()

    def write_record(self, table: str, columns: list, values: list):

        if len(columns) != len(values):
            raise ValueError('Columns and values not matching.')
        
        elif len(columns) > len(list(self.cursor.columns(table=table))):
            raise ValueError('Attempting to insert more columns than what is in the table.')
        
        else:
            query = f'INSERT INTO {table} ({", ".join(columns)}) VALUES ({", ".join(["?" for _ in values])})'
            self.cursor.execute(query, tuple(values))
            self.cursor.commit()

    def last_week_records(self, date_column: str, table: str):

        target_date = (datetime.date.today() - datetime.timedelta(7)).strftime('%Y-%m-%d')

        query_1 = f"SELECT * FROM {table} WHERE {date_column} >= '{target_date}';"
        self.cursor.execute(query_1)
        rows = self.cursor.fetchall()

        query_2 = f"SELECT name FROM sys.columns WHERE object_id = OBJECT_ID('{table}')"
        self.cursor.execute(query_2)
        col = self.cursor.fetchall()
        col = [x[0] for x in col]

        return pd.DataFrame.from_records(rows, columns=col)
    
    def close_db(self):

        self.cursor.close()
        self.conn.close()