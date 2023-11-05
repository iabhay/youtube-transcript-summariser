from config.config import Config
from database.db_ops.users_db import UsersDB


class UsersHelper:
    def __init__(self, uid):
        self.user = UsersDB(uid)
        self.uid = uid

    def upgrade_to_premium(self):
        ask = int(input(Config.UPGRADE_TO_PREMIUM_PROMPT))
        if ask == 1:
            self.user.update_user("role", "premiumuser")
            print("You are now upgraded to premium.")
            # self.premium_user.premium_module()
        return False

    def downgrade_to_basic(self):
        ask = int(input(Config.CONFIRM_PROMPT))
        if ask == 1:
            self.user.update_user("role", "nonpremiumuser")
            print("You are downgraded!!")
            # self.non_premium_obj.non_premium_module()