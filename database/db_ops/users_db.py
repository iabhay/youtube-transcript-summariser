from shortuuid import ShortUUID
from datetime import datetime
from database.database_query import UsersTableQuery, UserSearchesTableQuery, MessageTableQuery,HistoryTableQuery, PremiumListingTable,BannedUrlTable
from database.db_ops.db_helper import DBHelper
# from utils.Exception_Handler.sql_exception_handler import exception_handler
from config.config import Config

class UsersDB:
    def __init__(self, uid):
        self.uid = uid
        tm = datetime.now()
        self.dt_string = tm.strftime("%d/%m/%Y %H:%M:%S")
        self.uname = ""

    def create_user(self, username, password):
        self.uid = "U" + ShortUUID("123456789").random(length=4)
        sid = "S" + ShortUUID("123456789").random(length=4)
        DBHelper.save_data(UsersTableQuery.query_insert_user, (self.uid, self.dt_string, username, password))
        DBHelper.save_data(UserSearchesTableQuery.query_insert_user_search, (sid, self.dt_string, self.uid))

    def check_user(self, username, password):
        entry = DBHelper.fetch_data(UsersTableQuery.query_select_user, (username, password))
        if entry:
            self.uid = entry[0]
        return entry


    def update_user(self, field, value):
        # entry = self.check_user(username, password)
        if field == "role":
            DBHelper.save_data(UsersTableQuery.query_update_user_role, (value, self.uid))
        elif field == "ban_status":
            DBHelper.save_data(UsersTableQuery.query_update_user_ban_status, (value, self.uid))


    def fetch_user_details(self, uid):
        DBHelper.fetch_data(UsersTableQuery.query_select_user_by_uid, (uid,))

    def update_user_role_by_admin(self, username, role):
        DBHelper.save_data(UsersTableQuery.query_update_user_role, (role, username))


    def user_history(self, urlid):
        hid = "H" + ShortUUID("123456789").random(length=4)
        DBHelper.save_data(HistoryTableQuery.query_insert_history, (hid, self.dt_string, self.uid, urlid))

