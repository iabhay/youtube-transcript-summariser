import random

from transcript_handler.transcript_generator import transcriptor
from summary_handler.summary_generator import Summariser
from database.db_ops.users_db import UsersDB
from config.config import Config
from content_checker.content_check import ContentChecker
from database.db_ops.ban_url_db import BanUrlDB
from users.premium_user.premium_user_controller import PremiumUserController
from database.db_ops.searches_db import SearchesDB
from users.non_premium_user.non_premium_controller import NonPremiumUserController
class PremiumUser:
    def __init__(self, uid):
        self.uid = uid
        self.user = UsersDB(self.uid)
        self.transcript_obj = transcriptor()
        self.summary_obj = Summariser()
        self.content_check_obj = ContentChecker()
        self.ban_url_obj = BanUrlDB()
        self.premium_obj = PremiumUserController(self.uid)
        self.search_count_db = SearchesDB(self.uid)
        self.non_premium_obj = NonPremiumUserController(self.uid)

    def premium_module(self):
        print(f"Premium Plan - Basic User")
        while True:
            ask = int(input(Config.PREMIUM_PROMPT))
            if ask == 6:
                print("Exiting login Menu.!!")
            if ask == 1:
                res = self.submit_video()
                if res == "Logout":
                    print("You are banned")
                elif res == "1":
                    continue
                elif res:
                    self.non_premium_obj.non_premium_module()
                else:
                    print("Content is Blocked!")
            elif 2 <= ask <= 4:
                self.premium_obj.premium_controller(ask)
            elif ask == 5:
                self.downgrade_to_premium()
                print("Please login again.")
                break
            elif ask == 6:
                print(f"Exiting Menu!!")
                break
            else:
                print("Please Select Carefully!")

    def submit_video(self):
        return self.non_premium_obj.submit_video(self.uid)
    def downgrade_to_premium(self):
        ask = int(input("Are you Sure?\n1. Yes\n2. No"))
        if ask == 1:
            self.user.update_user("role", "nonpremiumuser")
