from config.config import Config
from utils.dicts import AdminMap


class Admin:
    def __init__(self, uid):
        self.uid = uid
        self.adm = AdminMap(self.uid)
        self.adm_menu = self.adm.admin_menu()
        self.message_menu = self.adm.message_menu()

    def adminmodule(self):
        while True:
            ask_user = int(input(Config.ADMIN_PROMPT))
            if ask_user == int(Config.ADMIN_PROMPT_LENGTH):
                print(Config.EXITING_PROMPT)
                break
            # message sub menu module
            elif ask_user == 9:
                self.messages_handler()
            elif (0 < ask_user <= len(self.adm_menu)) and ask_user != 9:
                # using dictionary - functionality mapping
                self.adm_menu[ask_user]()
            else:
                print(Config.INVALID_INPUT_PROMPT)

    def messages_handler(self):
        while True:
            ask = int(input(Config.MESSAGES_VIEW_PROMPT))
            if ask == int(Config.MESSAGES_VIEW_PROMPT_LENGTH):
                break
            elif 0 < ask <= len(self.message_menu):
                self.message_menu[ask]()
            else:
                print(Config.INVALID_INPUT_PROMPT)



