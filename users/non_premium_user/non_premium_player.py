from transcript_handler.transcript_generator import transcriptor
from summary_handler.summary_generator import Summariser
from database.db_ops.users_db import UsersDB
from config.config import Config
from content_checker.content_check import ContentChecker
from database.db_ops.ban_url_db import BanUrlDB
from users.non_premium_user.non_premium_controller import NonPremiumUserController
from database.db_ops.searches_db import SearchesDB


class NonPremiumUser:
    def __init__(self, uid):
        self.uid = uid
        self.user = UsersDB(self.uid)
        self.non_premium_obj = NonPremiumUserController(self.uid)

    def non_premium_module(self):
        print(f"Current Plan - Basic User\n")
        while True:
            ask = int(input(Config.NON_PREMIUM_PROMPT))
            if ask == 3:
                print("Exiting login Menu.!!")
                break
            elif ask == 1:
                res = self.non_premium_obj.submit_video(self.uid)
                if res:
                    if res == "Logout":
                        print("You are Banned")
                        break
                    elif res == "1":
                        continue
                    elif res:
                        self.non_premium_obj.non_premium_module()
                else:
                    print("Bad Content")
            elif ask == 2:
                self.upgrade_to_premium()
                print("Please login again.")
                break
            else:
                print("Please Select Carefully!")

    def upgrade_to_premium(self):
        ask = int(input(Config.UPGRADE_TO_PREMIUM_PROMPT))
        if ask == 1:
            self.user.update_user("role", "premiumuser")
