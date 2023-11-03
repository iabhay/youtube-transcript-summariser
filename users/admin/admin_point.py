from users.admin.admincontroller import AdminController
from config.config import Config

class Admin:
    def __init__(self, uid):
        self.uid = uid
        self.adm = AdminController(self.uid)
        self.admin_dict = {
            1: self.adm.view_user,
            2: self.adm.view_all_users,
            3: self.adm.downgrade_premium_user,
            4: self.adm.ban_user,
            5: self.adm.unban_user,
            6: self.adm.ban_url,
            7: self.adm.unban_url,
            8: self.adm.unban_url_for_premium_user,
            10: self.adm.view_history_of_user,
            11: self.adm.view_all_history,
            12: self.adm.view_premium_listing_of_user,
            13: self.adm.view_all_premium_listings,
            14: self.adm.show_all_ban_urls,
            15: self.adm.show_ban_url
        }

    def adminmodule(self):
        # try:
        ask_user = int(input(Config.ADMIN_PROMPT))
        if ask_user == 17:
            print("Exiting admin Module: ")
        while ask_user != 16:
            if ask_user == 9:
                self.messages_handler()
            elif 1 <= ask_user < 16:
                self.admin_dict[ask_user]()
            elif ask_user == 17:
                print("Exiting admin Module: ")
            else:
                print("Select Carefully!")
            ask_user = int(input(Config.ADMIN_PROMPT))
        #
        # except Exception:
        #     print(Exception.__name__)
        #     print("admin Module Controller not working!!")

    def messages_handler(self):
        message_views = {
            1: self.adm.messages_from_premium_users,
            2: self.adm.messages_from_non_premium_users,
            3: self.adm.message_from_user,
            4: self.adm.view_all_messages
        }
        while True:
            ask = int(input(Config.MESSAGES_VIEW_PROMPT))
            if ask == 5:
                break
            elif 0 < ask < 5:
                message_views[ask]()
            else:
                print("Please Select Carefully")



