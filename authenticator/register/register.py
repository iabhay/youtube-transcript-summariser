import hashlib
from pwinput import pwinput
from config.config import Config
from utils.password_validator import password_validation
from database.db_ops.users_db import UsersDB


class Register:
    def __init__(self):
        self.user = UsersDB("")

    def register_module(self):
        username = input("Enter username: ")
        print(Config.SECURE_PASSWORD_PROMPT)
        password = pwinput("Enter Password: ", mask="*")
        hashed_password = ""
        if not password_validation(password):
            print("Invalid Password!!")
        else:
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            if not self.check_registration(username, hashed_password):
            # try:
                self.user.create_user(username, hashed_password)
                print("Registered successfully!!")
            # except Exception:
            #     print(Exception.__name__)
            #     print("Data not registered successfully.")

    def check_registration(self, name, password):
        is_already_registered = self.user.check_user(name, password)
        # print(is_already_registered)
        if is_already_registered:
            print("Already registered!!\nTry login!!")
            return True
        else:
            return False