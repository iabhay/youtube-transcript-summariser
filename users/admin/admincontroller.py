from config.config import Config
from database.db_ops.db_helper import DBHelper
from database.db_ops.messages_db import MessageDB
from database.database_query import AdminQueries, UsersTableQuery
from database.db_ops.users_db import UsersDB
from database.db_ops.ban_url_db import BanUrlDB
from transcript_handler.transcript_generator import transcriptor
from database.db_ops.premium_listing_db import PremiumListingsDB
from database.db_ops.db_helper import DBHelper
from database.database_query import UsersTableQuery
from database.db_ops.history_db import HistoryDB


class AdminController:
    def __init__(self, uid):
        self.uid = uid
        self.msg_obj = MessageDB(self.uid)
        self.ban_url_obj = BanUrlDB()
        self.trancriptor = transcriptor()
        self.premium_listing_obj = PremiumListingsDB(self.uid)
    def view_user(self):
        username = input("Enter username: ")
        valid = self.uid_generator(username)
        if not valid:
            print("No such User found")
        else:
            target_uid = valid[0]
            table_schema = ['Uid', 'Username', 'Registered on', 'Role', 'Ban Status', 'Date', 'Today Search Count']
            DBHelper.display_data(AdminQueries.query_view_user, table_schema, (target_uid,))
    def view_all_users(self):
        table_schema = ['Uid', 'Username', 'Registered on', 'Role', 'Ban Status', 'Date', 'Today Search Count']
        DBHelper.display_data(AdminQueries.query_view_all_users, table_schema)
    def downgrade_premium_user(self):
        username = input("Enter username: ")
        valid = self.uid_generator(username)
        if not valid:
            print("No such User found")
        else:
            target_uid = valid[0]
            user_obj = UsersDB(target_uid)
            user_obj.update_user("role", "nonpremiumuser")
    def ban_user(self):
        username = input("Enter username: ")
        valid = self.uid_generator(username)
        if not valid:
            print("No such User found")
        else:
            target_uid = valid[0]
            user_obj = UsersDB(target_uid)
            user_obj.update_user("ban_status", "banned")
    def unban_user(self):
        username = input("Enter username: ")
        valid = self.uid_generator(username)
        if not valid:
            print("No such User found")
        else:
            target_uid = valid[0]
            user_obj = UsersDB(target_uid)
            user_obj.update_user("ban_status", "unbanned")
    def ban_url(self):
        ask = input("Enter URL : ")
        urlid = self.trancriptor.extract_video_id(ask)
        self.ban_url_obj.save_ban_url(urlid, "Admin", "5")

    def unban_url(self):
        ask = input("Enter URL : ")
        urlid = self.trancriptor.extract_video_id(ask)
        entry = self.ban_url_obj.view_ban_url(urlid)
        if entry:
            self.ban_url_obj.delete_ban_url(urlid)
        else:
            print("No Such Banned URL Found")

    def unban_url_for_premium_user(self):
        ask = input("Enter URL : ")
        username = input("Enter Username: ")
        valid = self.uid_generator(username)
        if valid:
            target_uid = valid[0]
            urlid = self.trancriptor.extract_video_id(ask)
            entry = self.ban_url_obj.view_ban_url(urlid)
            if entry:
                self.premium_listing_obj.remove_premium_listing(target_uid)
            else:
                print("No Such Banned URL Found")
        else:
            print("No Such User Found")
    def message_from_user(self):
        username = input("Enter username: ")
        self.msg_obj.view_one_message(username)
    def messages_from_non_premium_users(self):
        # choice = self.message_filter()
        # if choice == 0:
        #     pass
        # elif choice == 1:
        #     pass
        self.msg_obj.view_non_premium_messages()
    def messages_from_premium_users(self):
        # choice = self.message_filter()
        # if choice == 0:
        #     pass
        # elif choice == 1:
        #     pass
        self.msg_obj.view_premium_messages()
    def view_all_messages(self):
        # choice = self.message_filter()
        # if choice == 0:
        #     pass
        # elif choice == 1:
        #     pass
        self.msg_obj.view_all_messages()
    # def message_filter(self):
    #     ask = int(input(Config.MESSAGES_FILTER))
    #     pass

    def uid_generator(self, username):
        target = DBHelper.fetch_data(UsersTableQuery.query_select_user_by_admin, (username,))
        if target:
            return target[0]
        return

    def view_history_of_user(self):
        username = input("Enter Username: ")
        valid = self.uid_generator(username)
        if not valid:
            print("No such User found")
        else:
            target_uid = valid[0]
            history_obj = HistoryDB(target_uid)
            history_obj.view_one_user_history()


    def view_premium_listing_of_user(self):
        username = input("Enter Username: ")
        valid = self.uid_generator(username)
        if not valid:
            print("No such User found")
        else:
            target_uid = valid[0]
            premium_listing_obj = PremiumListingsDB(target_uid)
            premium_listing_obj.view_premium_user_listing()


    def view_all_history(self):
        history_obj = HistoryDB(self.uid)
        history_obj.view_all_history()

    def view_all_premium_listings(self):
        premium_listing_obj = PremiumListingsDB(self.uid)
        premium_listing_obj.view_all_premium_listings()

    def show_all_ban_urls(self):
        self.ban_url_obj.view_all_ban_urls()

    def show_ban_url(self):
        url = input("Enter URL : ")
        urlid = self.trancriptor.extract_video_id(url)
        entry = self.ban_url_obj.view_ban_url(urlid)
        entry_fetch = self.ban_url_obj.fetch_ban_url(urlid)
        if not entry_fetch:
            print("No Such Banned URL Found")
