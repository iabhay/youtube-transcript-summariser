import hashlib
from pwinput import pwinput
from database.db_ops.users_db import UsersDB
from users.premium_user.premium_user import PremiumUser
from users.admin.admin_point import Admin
from users.non_premium_user.non_premium_user import NonPremiumUser
from database.db_ops.messages_db import MessageDB
from config.config import Config


class Login:
    def __init__(self):
        self.uid = ""
        self.res = ""

    def login_module(self):
        while True:
            if self.res and self.uid and (self.res == "nonpremium" or self.res == "premium"):
                user = UsersDB(self.uid)
                if self.res == "premium":
                    non_premium_user = NonPremiumUser(self.uid)
                    self.res = non_premium_user.non_premium_module()
                elif self.res == "nonpremium":
                    premium_user = PremiumUser(self.uid)
                    self.res = premium_user.premium_module()
            elif self.res == True or self.res == False or self.res == "":
                username = input("Enter Your Name: ")
                password = pwinput(prompt="Enter your password:- ", mask="*")
                if username == Config.ADMIN_USERNAME and password == Config.ADMIN_PASSWORD:
                    admin = Admin("")
                    admin.adminmodule()
                    break
                else:
                    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                    user = UsersDB("")
                    entry = user.check_user(username, hashed_password)
                    if not entry:
                        print("Invalid Credentials!!")
                        return
                    uid = entry[0][0]
                    self.uid = uid
                    m_obj = MessageDB(uid)
                    non_premium_user = NonPremiumUser(uid)
                    premium_user = PremiumUser(uid)
                    admin = Admin(uid)
                    print("You are logged in!!")
                    # print(entry[0][4])
                    if entry[0][5] == "banned":
                        m_obj.banned_module()
                    elif entry[0][4] == "nonpremiumuser" and entry[0][5] == "unbanned":
                        self.res = non_premium_user.non_premium_module()
                        self.login_module()
                    elif entry[0][4] == "premiumuser" and entry[0][5] == "unbanned":
                        self.res = premium_user.premium_module()
                        self.login_module()
                    elif entry[0][4] == "admin":
                        admin.adminmodule()
                        break
                    else:
                        print("Wrong role was filled!")
                    return True
            elif not self.res:
                self.uid = ""
                self.res = ""
                break




