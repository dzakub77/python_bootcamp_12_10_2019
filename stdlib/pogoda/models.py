import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Tworze polaczenie z baza"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return conn

create_table_sql ="""
CREATE TABLE IF NOT EXISTS weather (
  id integer PRIMARY KEY,
  location_name text NOT NULL,
  temperature integer NOT NULL,
  date text NOT NULL
)
"""

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

if __name__ == "__main__":
    create_connection("test.db")
    create_table(conn, create_table_sql)
