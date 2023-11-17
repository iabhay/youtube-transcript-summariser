import logging
from config.config import Config
from database.db_ops.users_db import UsersDB
from config.log_config.log_config import LogStatements
logger = logging.getLogger('users_helper')


class UsersHelper:
    def __init__(self, uid):
        self.user = UsersDB(uid)
        self.uid = uid

    def upgrade_to_premium(self):
        try:
            ask = int(input(Config.UPGRADE_TO_PREMIUM_PROMPT))
            if 0 < ask < 3:
                if ask == 1:
                    self.user.update_user("role", "premiumuser")
                    return False
                elif ask == 2:
                    print("Back..")
            else:
                print("Enter valid choice.")
        except ValueError:
            print(Config.VALUE_ERROR_PROMPT)
        return None

    def downgrade_to_basic(self):
        try:
            ask = int(input(Config.CONFIRM_PROMPT))
            if 0 < ask < 3:
                if ask == 1:
                    self.user.update_user("role", "nonpremiumuser")
                    return False
                elif ask == 2:
                    print("back..")
            else:
                print("Enter valid choice.")
        except ValueError:
            print(Config.VALUE_ERROR_PROMPT)
        return None
