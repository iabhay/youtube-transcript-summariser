import logging
from shortuuid import ShortUUID
from datetime import datetime
from database.db_ops.db_helper import DBHelper
from database.database_query import PremiumListingTable
from utils.exception_handler import db_exception
from config.log_config.log_config import LogStatements
from config.config import Config
logger = logging.getLogger('premium_listing_db')

class PremiumListingsDB:
    def __init__(self, uid):
        self.uid = uid
        tm = datetime.now()
        self.dt_string = tm.strftime(Config.DATE_FORMAT)
        self.table_schema = ['Date', 'Username', 'Url']

    @db_exception(LogStatements.premium_listing_of_url, LogStatements.fail_premium_listing_of_url)
    def save_premium_url(self, urlid):
        if not self.check_premium_list_url(urlid):
            pid = "P" + ShortUUID(Config.SHORT_UID_CONSTRAINTS).random(length=4)
            DBHelper.save_data(PremiumListingTable.query_insert_premium_listing, (pid, self.dt_string, self.uid, urlid))

    @db_exception()
    def check_premium_list_url(self, urlid):
        return DBHelper.fetch_data(PremiumListingTable.query_select_premium_url_for_user, (urlid, self.uid))

    @db_exception()
    def view_premium_user_listing(self):
        DBHelper.display_data(PremiumListingTable.query_select_premium_listing, self.table_schema, (self.uid, ))

    @db_exception()
    def view_all_premium_listings(self):
        DBHelper.display_data(PremiumListingTable.query_select_all_premium_listing, self.table_schema)

    @db_exception(LogStatements.premium_unlisting_of_url, LogStatements.fail_premium_unlisting_of_url)
    def remove_premium_listing(self, uid):
        DBHelper.delete_data(PremiumListingTable.query_delete_premium_listing, (uid, ))