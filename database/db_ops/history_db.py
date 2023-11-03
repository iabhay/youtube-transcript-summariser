from datetime import datetime
from shortuuid import ShortUUID
from database.database_query import HistoryTableQuery
from database.db_ops.db_helper import DBHelper


class HistoryDB:
    def __init__(self, uid):
        self.uid = uid
        tm = datetime.now()
        self.dt_string = tm.strftime("%d/%m/%Y %H:%M:%S")

    def save_history(self, urlid):
        hid = "M" + ShortUUID("123456789").random(length=4)
        DBHelper.save_data(HistoryTableQuery.query_insert_history, (hid, self.dt_string, self.uid, urlid))


    def view_one_user_history(self):
        table_schema = ['Date', 'Url']
        DBHelper.display_data(HistoryTableQuery.query_select_history,table_schema, (self.uid,))

    def view_all_history(self):
        table_schema = ['Date','Username', 'URL']
        DBHelper.display_data(HistoryTableQuery.query_select_all_history, table_schema)
