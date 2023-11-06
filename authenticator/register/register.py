import hashlib
from pwinput import pwinput
from config.config import Config
from utils.password_validator import password_validation
from database.db_ops.users_db import UsersDB


class Register:
    def __init__(self):
        self.user = UsersDB("")

    def register_module(self):
        username = input(Config.ENTER_USERNAME_PROMPT)
        print(Config.SECURE_PASSWORD_PROMPT)
        password = pwinput(Config.ENTER_PASSWORD_PROMPT, mask="*")
        # Checking for regex validation
        if not password_validation(password):
            print("Invalid Password!!")
        else:
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            # checking if already registered with username
            if not self.check_registration(username, hashed_password):
                self.user.create_user(username, hashed_password)
                print("Registered successfully!!")

    def check_registration(self, name, password):
        is_already_registered = self.user.check_user(name, password)
        if is_already_registered:
            print("Already registered!!\nTry login!!")
            return True
        else:
            return False
