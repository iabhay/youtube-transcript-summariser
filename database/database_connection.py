import sqlite3
import logging
from config.log_config.log_config import LogStatements
logger = logging.getLogger('database_connection')


class DatabaseConnection:
    def __init__(self, host: str):
        self.connection = None
        self.host = host

    def __enter__(self) -> sqlite3.Connection:
        try:
            self.connection = sqlite3.connect(self.host)
            return self.connection
        except Exception as e:
            logger.debug(LogStatements.log_error_connecting_database)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
