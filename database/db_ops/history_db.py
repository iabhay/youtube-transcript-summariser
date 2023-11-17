import logging
from datetime import datetime
from shortuuid import ShortUUID
from database.database_query import HistoryTableQuery
from database.db_ops.db_helper import DBHelper
from utils.exception_handler import db_exception
from config.log_config.log_config import LogStatements
from config.config import Config
logger = logging.getLogger('history_db')


class HistoryDB:
    def __init__(self, uid):
        self.uid = uid
        tm = datetime.now()
        self.dt_string = tm.strftime(Config.DATE_FORMAT)

    @db_exception(LogStatements.user_history_saved, LogStatements.fail_user_history_saved)
    def save_history(self, urlid):
        hid = "H" + ShortUUID(Config.SHORT_UID_CONSTRAINTS).random(length=4)
        DBHelper.save_data(HistoryTableQuery.query_insert_history, (hid, self.dt_string, self.uid, urlid))
        return hid

    @db_exception("", LogStatements.log_exception_message)
    def view_one_user_history(self):
        table_schema = ['Date', 'Url']
        DBHelper.display_data(HistoryTableQuery.query_select_history, table_schema, (self.uid,))

    @db_exception("", LogStatements.log_exception_message)
    def view_all_history(self):
        table_schema = ['Date', 'Username', 'URL']
        DBHelper.display_data(HistoryTableQuery.query_select_all_history, table_schema)