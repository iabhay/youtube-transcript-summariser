# from utils.dicts import AuthMAP
from config.config import Config
from database.db_ops.db_initialise import DBInitialise
from utils.exception_handler import handle_exceptions
from authenticator.login.login import Login
from authenticator.register.register import Register

class YTTS:
    def __init__(self):
        register = Register()
        login = Login()
        self.auth_dict = {
            1: register.register_module,
            2: login.login_module
        }

    @handle_exceptions()
    def menu(self):
        print(Config.APP_INTRO)
        while True:
            ask = int(input(Config.MAIN_PROMPT))
            n = int(Config.MAIN_PROMPT_LENGTH)
            if ask == n:
                print(Config.APP_OUTRO)
                break
            elif 0 < ask <= len(self.auth_dict):
                self.auth_dict[ask]()
            else:
                print(Config.INVALID_INPUT_PROMPT)


if __name__ == "__main__":
    Config.load()
    DBInitialise.create_all_tables()
    ytts_obj = YTTS()
    ytts_obj.menu()


