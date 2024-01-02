import sqlite3
import pandas as pd

class local_db:
    def __init__(self):
        self.conn = sqlite3.connect('pd_storage')
        self.cursor = self.conn.cursor()
        self.check_table()
    
    def check_table(self):
        query = """
                SELECT name FROM sqlite_master WHERE
                type="table" and name="pd_table"
                """
        self.cursor.execute(query)
        self.exists = self.cursor.fetchone()
        if self.exists is None:
            create_table_query = """
                            CREATE TABLE pd_table (
                            complete_date DATE,
                            minutes INTEGER
                            )"""
            self.cursor.execute(create_table_query)
            
    def write_record(self, rec : list):
        insert_query = """
                    INSERT INTO pd_table 
                    (complete_date, minutes)
                    VALUES (?, ?)"""
        self.cursor.execute(insert_query, tuple(rec))
        self.conn.commit()

    def pull_records(self):
        pull_query = "SELECT * FROM pd_table"
        self.cursor.execute(pull_query)
        self.rows = self.cursor.fetchall()
        self.df = pd.DataFrame(self.rows, columns=['date', 'minutes'])
        return self.df

    def close_db(self):
        self.conn.close()

if __name__ == '__main__':
    db = local_db()
    db.write_record(['2023-12-28', 15])
    df = db.pull_records()
    print(df)
    db.close_db()