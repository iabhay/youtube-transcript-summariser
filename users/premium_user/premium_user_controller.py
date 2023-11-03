from config.config import Config
from database.db_ops.users_db import UsersDB
from users.non_premium_user.non_premium_controller import NonPremiumUserController
from database.db_ops.messages_db import MessageDB
from database.db_ops.premium_listing_db import PremiumListingsDB

class PremiumUserController:
    def __init__(self, uid):
        self.uid = uid
        self.msg_obj = MessageDB(uid)
        self.premium_obj = PremiumListingsDB(uid)

    def premium_controller(self, ask):
            if ask == 2:
                self.send_message_to_admin()
            elif ask == 3:
                self.premium_listing_of_banned_url()
            elif ask == 4:
                self.view_my_history()

    def send_message_to_admin(self):
        ask = input("Enter Message for admin")
        self.msg_obj.save_message(ask)

    def premium_listing_of_banned_url(self):
        url = input("Enter URL for premium listing")
        self.premium_obj.save_premium_url(url)

    def view_my_history(self):
        print(self.premium_obj.view_premium_user_listing())
