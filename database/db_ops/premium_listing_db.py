from shortuuid import ShortUUID
from datetime import datetime
from database.db_ops.db_helper import DBHelper
from database.database_query import PremiumListingTable


class PremiumListingsDB:
    def __init__(self, uid):
        self.uid = uid
        tm = datetime.now()
        self.dt_string = tm.strftime("%d/%m/%Y %H:%M:%S")

    def save_premium_url(self, urlid):
        if not self.check_premium_list_url(urlid):
            pid = "P" + ShortUUID("123456789").random(length=4)
            DBHelper.save_data(PremiumListingTable.query_insert_premium_listing, (pid, self.dt_string, self.uid, urlid))

    def check_premium_list_url(self, urlid):
        return DBHelper.fetch_data(PremiumListingTable.query_select_premium_url_for_user, (urlid, self.uid))

    def view_premium_user_listing(self):
        table_schema = ['Date', 'Username', 'Url']
        DBHelper.display_data(PremiumListingTable.query_select_premium_listing, table_schema, (self.uid, ))

    def view_all_premium_listings(self):
        table_schema = ['Date', 'Username', 'Url']
        DBHelper.display_data(PremiumListingTable.query_select_all_premium_listing, table_schema)

    def remove_premium_listing(self, uid):
        DBHelper.delete_data(PremiumListingTable.query_delete_premium_listing, (uid, ))