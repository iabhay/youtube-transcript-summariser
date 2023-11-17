from prettytable import PrettyTable
from database.database_connection import DatabaseConnection
import logging
from config.log_config.log_config import LogStatements
from config.config import Config
logger = logging.getLogger('db_helper')
YTTSDB = 'YTTSDB.db'


class DBHelper:
    @classmethod
    def save_data(cls, query: str, tup: tuple) -> None:
        with DatabaseConnection(YTTSDB) as connection:
            cursor = connection.cursor()
            cursor.execute(query, tup)

    @classmethod
    def fetch_data(cls, query: str, tup: tuple = None):
        with DatabaseConnection(YTTSDB) as connection:
            cursor = connection.cursor()
            if not tup:
                cursor.execute(query)
            else:
                cursor.execute(query, tup)
            return cursor.fetchall()

    @classmethod
    def display_data(cls, query: str, table_schema: list, value: tuple = None):
        with DatabaseConnection(YTTSDB) as connection:
            cursor = connection.cursor()
            if not value:
                var = cursor.execute(query)
            else:
                var = cursor.execute(query, value)
            if var is None:
                print(Config.NO_DATA_EXIST_PROMPT)
            else:
                table = PrettyTable(table_schema)
                rows = cursor.fetchall()
                if len(rows) == 0:
                    print(Config.NO_DATA_EXIST_PROMPT)
                else:
                    for row in rows:
                        table.add_row(row)
                    print(table)

    @classmethod
    def delete_data(cls, query: str, value: tuple):
        with DatabaseConnection(YTTSDB) as connection:
            cursor = connection.cursor()
            cursor.execute(query, value)
