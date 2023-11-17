import logging
from shortuuid import ShortUUID
from datetime import datetime
from database.database_query import UsersTableQuery, UserSearchesTableQuery,HistoryTableQuery
from database.db_ops.db_helper import DBHelper
# from utils.Exception_Handler.sql_exception_handler import exception_handler
from utils.exception_handler import db_exception
from config.log_config.log_config import LogStatements
from config.config import Config
logger = logging.getLogger('users_db')


class UsersDB:
    def __init__(self, uid):
        self.uid = uid
        tm = datetime.now()
        self.dt_string = tm.strftime(Config.DATE_FORMAT)
        self.uname = ""

    @db_exception(LogStatements.user_created, LogStatements.fail_user_created)
    def create_user(self, username, password):
        self.uid = "U" + ShortUUID(Config.SHORT_UID_CONSTRAINTS).random(length=4)
        sid = "S" + ShortUUID(Config.SHORT_UID_CONSTRAINTS).random(length=4)
        DBHelper.save_data(UsersTableQuery.query_insert_user, (self.uid, self.dt_string, username, password))
        DBHelper.save_data(UserSearchesTableQuery.query_insert_user_search, (sid, self.dt_string, self.uid))
        print(Config.REGISTRATION_SUCCESS_PROMPT)

    @db_exception()
    def check_user(self, username, password):
        entry = DBHelper.fetch_data(UsersTableQuery.query_select_user, (username, password))
        if entry:
            self.uid = entry[0]
        return entry

    @db_exception(LogStatements.user_updated, LogStatements.fail_user_updated)
    def update_user(self, field, value):
        if field == Config.ROLE_FIELD:
            DBHelper.save_data(UsersTableQuery.query_update_user_role, (value, self.uid))
            if value == Config.PREMIUM_USER_ROLE_NAME:
                logger.info(LogStatements.user_upgraded_to_premium)
                print(Config.UPGRADE_SUCCESS_PROMPT)
            elif value == Config.NON_PREMIUM_USER_ROLE_NAME:
                logger.info(LogStatements.user_downgraded_to_non_premium)
                print(Config.DOWNGRADE_SUCCESS_PROMPT)
        elif field == Config.BAN_STATUS_FIELD_NAME:
            DBHelper.save_data(UsersTableQuery.query_update_user_ban_status, (value, self.uid))

    @db_exception()
    def fetch_user_details(self, uid):
        DBHelper.fetch_data(UsersTableQuery.query_select_user_by_uid, (uid,))

    @db_exception(LogStatements.user_updated, LogStatements.fail_user_updated)
    def update_user_role_by_admin(self, username, role):
        DBHelper.save_data(UsersTableQuery.query_update_user_role, (role, username))

    @db_exception(LogStatements.user_history_saved, LogStatements.fail_user_history_saved)
    def user_history(self, urlid):
        hid = "H" + ShortUUID(Config.SHORT_UID_CONSTRAINTS).random(length=4)
        DBHelper.save_data(HistoryTableQuery.query_insert_history, (hid, self.dt_string, self.uid, urlid))
