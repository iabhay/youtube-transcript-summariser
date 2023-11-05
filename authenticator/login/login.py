import hashlib
from pwinput import pwinput
from database.db_ops.users_db import UsersDB
from users.premium_user.premium_user import PremiumUser
from users.admin.admin_point import Admin
from users.non_premium_user.non_premium_user import NonPremiumUser
from database.db_ops.messages_db import MessageDB
from config.config import Config


class Login:
    def login_module(self):
        username = input("Enter Your Name: ")
        password = pwinput(prompt="Enter your password:- ", mask="*")
        if username == Config.ADMIN_USERNAME and password == Config.ADMIN_PASSWORD:
            admin = Admin("")
            admin.adminmodule()
        else:
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            user = UsersDB("")
            entry = user.check_user(username, hashed_password)
            # print(entry)
            if not entry:
                print("Invalid Credentials!!")
                return
            uid = entry[0][0]
            m_obj = MessageDB(uid)
            non_premium_user = NonPremiumUser(uid)
            premium_user = PremiumUser(uid)
            admin = Admin(uid)
            print("You are logged in!!")
            # print(entry[0][4])
            if entry[0][5] == "banned":
                m_obj.banned_module()
            elif entry[0][4] == "nonpremiumuser" and entry[0][5] == "unbanned":
                non_premium_user.non_premium_module()
            elif entry[0][4] == "premiumuser" and entry[0][5] == "unbanned":
                premium_user.premium_module()
            elif entry[0][4] == "admin":
                admin.adminmodule()
            else:
                print("Wrong role was filled!")
            return True




