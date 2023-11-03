from datetime import datetime
from shortuuid import ShortUUID
from database.database_query import MessageTableQuery
from database.db_ops.db_helper import DBHelper


class MessageDB:
    def __init__(self, uid):
        self.uid = uid
        tm = datetime.now()
        self.dt_string = tm.strftime("%d/%m/%Y %H:%M:%S")

    def banned_module(self):
        message = input("Send Message to Admin for Unban: ")
        try:
            self.save_message(message)
            print("Successfully sent message.")
        except:
            raise Exception("Message not sent successfully.")

    def save_message(self, description):
        mid = "M" + ShortUUID("123456789").random(length=4)
        DBHelper.save_data(MessageTableQuery.query_insert_message, (mid, self.dt_string, self.uid, description))

    def delete_message_by_admin(self):
        DBHelper.delete_data(MessageTableQuery.query_delete_message, (self.uid,))

    def view_one_message(self, username):
        table_schema = ['Date', 'Username', 'Description']
        DBHelper.display_data(MessageTableQuery.query_select_message, table_schema, (username,))

    def view_premium_messages(self):
        table_schema = ['Date', 'Username', 'Description']
        DBHelper.display_data(MessageTableQuery.query_select_premium_message, table_schema)

    def view_non_premium_messages(self):
        table_schema = ['Date', 'Username', 'Description']
        DBHelper.display_data(MessageTableQuery.query_select_non_premium_message, table_schema)

    def view_all_messages(self):
        table_schema = ['Date', 'Username', 'Description']
        DBHelper.display_data(MessageTableQuery.query_select_all_messages, table_schema)
