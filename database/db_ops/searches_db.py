import logging
from datetime import datetime
from database.db_ops.db_helper import DBHelper
from database.database_query import UserSearchesTableQuery
from database.db_ops.users_db import UsersDB
from utils.exception_handler import db_exception
from config.log_config.log_config import LogStatements
logger = logging.getLogger('searches_db')


class SearchesDB:
    def __init__(self, uid):
        self.uid = uid
        tm = datetime.now()
        self.dt_string = tm.strftime("%d/%m/%Y %H:%M:%S")
        self.user = UsersDB(self.uid)
        entry = DBHelper.fetch_data(UserSearchesTableQuery.query_select_user_search, (self.uid,))
        if entry[0][3] > self.dt_string:
            DBHelper.save_data(UserSearchesTableQuery.query_update_day_wise, (self.dt_string, 0))

    @db_exception()
    def view_user_search_count(self):
        # try:
        entry = DBHelper.fetch_data(UserSearchesTableQuery.query_select_user_search, (self.uid,))
        return entry[0][2]
        # except Exception as e:
        #     logger.debug(LogStatements.log_exception_message)
        # else:

    @db_exception(default_success_response=LogStatements.search_count_updated,default_failure_response=LogStatements.fail_search_count_updated)
    def update_user_search_count(self, limit):
        count = self.view_user_search_count() + 1
        # try:
        DBHelper.save_data(UserSearchesTableQuery.query_update_user_search_count, (count, self.uid))
        if count > limit:
            self.user.update_user("ban_status", "banned")
            return False
        return True
        # except Exception as e:
        #     logger.debug(LogStatements.fail_search_count_updated)
