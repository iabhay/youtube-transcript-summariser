from database.db_ops.messages_db import MessageDB
from database.db_ops.premium_listing_db import PremiumListingsDB
from database.db_ops.history_db import HistoryDB


class PremiumUserController:
    def __init__(self, uid):
        self.uid = uid
        self.msg_obj = MessageDB(uid)
        self.premium_obj = PremiumListingsDB(uid)
        self.history_obj = HistoryDB(uid)

    def send_message_to_admin(self, url=""):
        ask = input("Enter Message for admin: ")
        # if url is given that means premium listing message
        if len(url) > 0:
            ask = ask + ", Url for premium listing -> " + url
        self.msg_obj.save_message(ask)
        print("Message sent successfully.")
        return None

    def premium_listing_of_banned_url(self):
        url = input("Enter URL for premium listing: ")
        self.send_message_to_admin(url)
        print("Once approved by admin, it'll be added to your premium listing.")
        return None

    def view_my_premium_listing(self):
        self.premium_obj.view_premium_user_listing()
        return None

    def view_my_history(self):
        self.history_obj.view_one_user_history()
        return None