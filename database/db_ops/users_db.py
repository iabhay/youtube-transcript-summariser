import logging
from shortuuid import ShortUUID
from datetime import datetime
from database.database_query import UsersTableQuery, UserSearchesTableQuery,HistoryTableQuery
from database.db_ops.db_helper import DBHelper
# from utils.Exception_Handler.sql_exception_handler import exception_handler
from utils.exception_handler import db_exception
from config.log_config.log_config import LogStatements
logger = logging.getLogger('users_db')


class UsersDB:
    def __init__(self, uid):
        self.uid = uid
        tm = datetime.now()
        self.dt_string = tm.strftime("%d/%m/%Y %H:%M:%S")
        self.uname = ""

    @db_exception(LogStatements.user_created, LogStatements.fail_user_created)
    def create_user(self, username, password):
        self.uid = "U" + ShortUUID("123456789").random(length=4)
        sid = "S" + ShortUUID("123456789").random(length=4)
        # try:
        DBHelper.save_data(UsersTableQuery.query_insert_user, (self.uid, self.dt_string, username, password))
        DBHelper.save_data(UserSearchesTableQuery.query_insert_user_search, (sid, self.dt_string, self.uid))
        print("Registered successfully!!")
        #     logger.info(LogStatements.user_created)
        # except Exception as e:
        #     logger.debug(LogStatements.fail_user_created)

    @db_exception()
    def check_user(self, username, password):
        entry = DBHelper.fetch_data(UsersTableQuery.query_select_user, (username, password))
        if entry:
            self.uid = entry[0]
        return entry

    def update_user(self, field, value):
        # entry = self.check_user(username, password)
        try:
            if field == "role":
                DBHelper.save_data(UsersTableQuery.query_update_user_role, (value, self.uid))
                if value == "premiumuser":
                    logger.info(LogStatements.user_upgraded_to_premium)
                    print("You are now upgraded to premium.")
                elif value == "nonpremiumuser":
                    logger.info(LogStatements.user_downgraded_to_non_premium)
                    print("You are downgraded!!")
            elif field == "ban_status":
                DBHelper.save_data(UsersTableQuery.query_update_user_ban_status, (value, self.uid))
                logger.info(LogStatements.user_updated)
        except Exception as e:
            logger.debug(LogStatements.fail_user_updated)

    @db_exception()
    def fetch_user_details(self, uid):
        # try:
        DBHelper.fetch_data(UsersTableQuery.query_select_user_by_uid, (uid,))
        # except Exception as e:
        #     logger.debug(LogStatements.log_exception_message)

    @db_exception(LogStatements.user_updated, LogStatements.fail_user_updated)
    def update_user_role_by_admin(self, username, role):
        # try:
        DBHelper.save_data(UsersTableQuery.query_update_user_role, (role, username))
        #     logger.info(LogStatements.user_updated)
        # except Exception as e:
        #     logger.debug(LogStatements.fail_user_updated)

    @db_exception(LogStatements.user_history_saved, LogStatements.fail_user_history_saved)
    def user_history(self, urlid):
        # try:
        hid = "H" + ShortUUID("123456789").random(length=4)
        DBHelper.save_data(HistoryTableQuery.query_insert_history, (hid, self.dt_string, self.uid, urlid))
        #     logger.info(LogStatements.user_history_saved)
        # except Exception as e:
        #     logger.debug(LogStatements.fail_user_history_saved)
