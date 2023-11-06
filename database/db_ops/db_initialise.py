from database.database_query import CreateTablesQuery
from database.database_connection import DatabaseConnection
import logging
from config.log_config.log_config import LogStatements
logger = logging.getLogger('db_initialise')
class DBInitialise:
    @classmethod
    def create_all_tables(cls) -> None:
        try:
            with DatabaseConnection('YTTSDB.db') as connection:
                cursor = connection.cursor()
                cursor.execute(CreateTablesQuery.query_create_user)
                cursor.execute(CreateTablesQuery.query_create_history)
                cursor.execute(CreateTablesQuery.query_create_message)
                cursor.execute(CreateTablesQuery.query_create_ban_url)
                cursor.execute(CreateTablesQuery.query_create_user_search)
                cursor.execute(CreateTablesQuery.query_create_premium_listing)
                logger.info(LogStatements.tables_created)
        except Exception as e:
            logger.debug(LogStatements.fail_tables_created)
