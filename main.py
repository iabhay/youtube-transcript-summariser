# from summary_handler.summary_generator import summarise
from register.register import Register
from login.login import Login
from config.config import Config
from database.db_ops.db_initialise import DBInitialise

class YTTS:
    def __init__(self):
        self.register = Register()
        self.login = Login()
        # obj = summarise()
        # obj.analyze_text()

    def menu(self):
        print("Transcriptor  : Smart Video, Simply Summarised!!")
        ask = int(input(Config.MAIN_PROMPT))
        if 1 > ask or ask > 2:
            print("Bye! Thanks for using.")
        while 0 < ask < 3:
            if ask == 1:
                self.register.register_module()
            elif ask == 2:
                self.login.login_module()
            else:
                print("Please Select Carefully!")
            ask = int(input(Config.MAIN_PROMPT))
            if ask == 3:
                print("Bye! Thanks for using.")


if __name__ == "__main__":
    # Config = Config.load()
    Config.load()
    DBInitialise.create_all_tables()
    ytts_obj = YTTS()
    ytts_obj.menu()
