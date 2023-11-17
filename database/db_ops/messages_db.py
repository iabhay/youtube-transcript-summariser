import logging
from datetime import datetime
from shortuuid import ShortUUID
from database.database_query import MessageTableQuery
from database.db_ops.db_helper import DBHelper
from utils.exception_handler import db_exception
from config.log_config.log_config import LogStatements
from config.config import Config
logger = logging.getLogger('messages_db')

class MessageDB:
    def __init__(self, uid):
        self.uid = uid
        tm = datetime.now()
        self.dt_string = tm.strftime(Config.DATE_FORMAT)
        self.table_schema = ['Date', 'Username', 'Description']

    @db_exception(LogStatements.message_sent, LogStatements.fail_message_sent)
    def banned_module(self):
        message = input("Send Message to Admin for Unban: ")
        self.save_message(message)
        print("Successfully sent message.")

    @db_exception(LogStatements.message_sent, LogStatements.fail_message_sent)
    def save_message(self, description):
        mid = "M" + ShortUUID(Config.SHORT_UID_CONSTRAINTS).random(length=4)
        DBHelper.save_data(MessageTableQuery.query_insert_message, (mid, self.dt_string, self.uid, description))

    @db_exception(LogStatements.message_delete, LogStatements.fail_message_delete)
    def delete_message_by_admin(self):
        DBHelper.delete_data(MessageTableQuery.query_delete_message, (self.uid,))

    @db_exception()
    def view_one_message(self, username):
        DBHelper.display_data(MessageTableQuery.query_select_message, self.table_schema, (username,))

    @db_exception()
    def view_premium_messages(self):
        DBHelper.display_data(MessageTableQuery.query_select_premium_message, self.table_schema)

    @db_exception()
    def view_non_premium_messages(self):
        DBHelper.display_data(MessageTableQuery.query_select_non_premium_message, self.table_schema)

    @db_exception()
    def view_all_messages(self):
        DBHelper.display_data(MessageTableQuery.query_select_all_messages, self.table_schema)
