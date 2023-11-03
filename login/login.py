import hashlib
from pwinput import pwinput
from database.db_ops.users_db import UsersDB
from users.premium_user.premium_user import PremiumUser
from users.admin.admin_point import Admin
from users.non_premium_user.non_premium_player import NonPremiumUser
from database.db_ops.messages_db import MessageDB


class Login:
    def __init__(self):
        self.user = UsersDB("")
        self.non_premium_user = ""
        self.premium_user = ""
        self.admin = Admin("")
        self.uid = ""

    def login_module(self):
        username = input("Enter Your Name: ")
        password = pwinput(prompt="Enter your password:- ", mask="*")
        if username == "admin" and password == "admin":
            self.admin.adminmodule()
        else:
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            entry = self.user.check_user(username, hashed_password)
            # print(entry)
            if not entry:
                print("Invalid Credentials!!")
            else:
                self.uid = entry[0][0]
                self.m_obj = MessageDB(self.uid)
                self.non_premium_user = NonPremiumUser(self.uid)
                self.premium_user = PremiumUser(self.uid)
                admin = Admin(self.uid)
                print("You are logged in!!")
                if entry[0][5] == "banned":
                    self.m_obj.banned_module()
                elif entry[0][4] == "nonpremiumuser" and entry[0][5] == "unbanned":
                    self.non_premium_user.non_premium_module()
                elif entry[0][4] == "premiumuser" and entry[0][5] == "unbanned":
                    self.premium_user.premium_module()
                elif entry[0][4] == "admin":
                    admin.adminmodule()
                else:
                    print("Wrong role was filled!")




