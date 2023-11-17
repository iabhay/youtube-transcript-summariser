import logging
from shortuuid import ShortUUID
from datetime import datetime
from database.db_ops.db_helper import DBHelper
from database.database_query import BannedUrlTable
from utils.exception_handler import db_exception
from config.log_config.log_config import LogStatements
from config.config import Config
logger = logging.getLogger('ban_url_db')
class BanUrlDB:
    def __init__(self):
        self.uid = ""
        self.uname = ""
        self.table_schema = ['URL ID', 'Category', 'Severity']

    @db_exception(LogStatements.url_banned, LogStatements.fail_url_banned)
    def save_ban_url(self, urlid, category, severity):
        if not self.fetch_ban_url(urlid):
            bid = "B" + ShortUUID(Config.SHORT_UID_CONSTRAINTS).random(length=4)
            DBHelper.save_data(BannedUrlTable.query_insert_ban_url, (bid, urlid, category, severity))

    @db_exception()
    def fetch_ban_url(self, urlid):
        return DBHelper.fetch_data(BannedUrlTable.query_select_ban_url, (urlid, ))

    @db_exception(LogStatements.url_unbanned, LogStatements.fail_url_banned)
    def delete_ban_url(self, urlid):
        DBHelper.delete_data(BannedUrlTable.query_unban_url, (urlid,))

    @db_exception()
    def view_ban_url(self, urlid):
        DBHelper.display_data(BannedUrlTable.query_select_ban_url, self.table_schema, (urlid,))

    @db_exception()
    def check_ban_url(self, urlid):
        return DBHelper.fetch_data(BannedUrlTable.query_select_ban_url, (urlid, ))

    @db_exception()
    def view_all_ban_urls(self):
        return DBHelper.display_data(BannedUrlTable.query_select_all_ban_url, self.table_schema)
