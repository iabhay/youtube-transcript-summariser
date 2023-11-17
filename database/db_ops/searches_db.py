import logging
from datetime import datetime
from database.db_ops.db_helper import DBHelper
from database.database_query import UserSearchesTableQuery
from database.db_ops.users_db import UsersDB
from utils.exception_handler import db_exception
from config.log_config.log_config import LogStatements
from config.config import Config
logger = logging.getLogger('searches_db')


class SearchesDB:
    @db_exception()
    def __init__(self, uid):
        self.uid = uid
        tm = datetime.now()
        self.dt_string = tm.strftime(Config.DATE_FORMAT)
        self.user = UsersDB(self.uid)
        entry = DBHelper.fetch_data(UserSearchesTableQuery.query_select_user_search, (self.uid,))
        if entry[0][3] > self.dt_string:
            DBHelper.save_data(UserSearchesTableQuery.query_update_day_wise, (self.dt_string, 0))

    @db_exception()
    def view_user_search_count(self):
        entry = DBHelper.fetch_data(UserSearchesTableQuery.query_select_user_search, (self.uid,))
        return entry[0][2]

    @db_exception(default_success_response=LogStatements.search_count_updated,default_failure_response=LogStatements.fail_search_count_updated)
    def update_user_search_count(self, limit):
        count = self.view_user_search_count() + 1
        DBHelper.save_data(UserSearchesTableQuery.query_update_user_search_count, (count, self.uid))
        if count > limit:
            self.user.update_user(Config.BAN_STATUS_FIELD_NAME, Config.BANNED_FIELD_NAME)
            return False
        return True
