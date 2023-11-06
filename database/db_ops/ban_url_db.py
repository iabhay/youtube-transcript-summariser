from shortuuid import ShortUUID
from datetime import datetime
from database.db_ops.db_helper import DBHelper
from database.database_query import BannedUrlTable

class BanUrlDB:
    def __init__(self):
        self.uid = ""
        tm = datetime.now()
        self.dt_string = tm.strftime("%d/%m/%Y %H:%M:%S")
        self.uname = ""

    def save_ban_url(self, urlid, category, severity):
        if not self.fetch_ban_url(urlid):
            bid = "B" + ShortUUID("123456789").random(length=4)
            DBHelper.save_data(BannedUrlTable.query_insert_ban_url, (bid, urlid, category, severity))

    def fetch_ban_url(self, urlid):
        return DBHelper.fetch_data(BannedUrlTable.query_select_ban_url, (urlid, ))

    def delete_ban_url(self, urlid):
        DBHelper.delete_data(BannedUrlTable.query_unban_url, (urlid,))

    def view_ban_url(self, urlid):
        table_schema = ['URL ID', 'Category', 'Severity']
        DBHelper.display_data(BannedUrlTable.query_select_ban_url, table_schema, (urlid,))

    def view_all_ban_urls(self):
        table_schema = ['URL ID', 'Category', 'Severity']
        return DBHelper.display_data(BannedUrlTable.query_select_all_ban_url, table_schema)