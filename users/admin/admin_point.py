from config.config import Config
from utils.dicts import AdminMap
from utils.exception_handler import handle_exceptions

class Admin:
    def __init__(self, uid):
        self.uid = uid
        self.adm = AdminMap(self.uid)
        self.message_menu = self.adm.message_menu()
        self.admin_user_menu = self.adm.user_ops_menu()
        self.admin_url_menu = self.adm.url_ops_menu()
        self.admin_premiumlisting_menu = self.adm.premiumlisting_ops_menu()
        self.admin_history_menu = self.adm.history_ops_menu()

    def adminmodule(self):
        while True:
            try:
                ask_user = int(input(Config.ADMIN_UPDATED_MENU))
                if ask_user == int(Config.ADMIN_UPDATED_MENU_LENGTH):
                    print(Config.EXITING_PROMPT)
                    break
                #user, url, premium,message, history
                elif ask_user == 1:
                    self.user_handler()
                elif ask_user == 2:
                    self.url_handler()
                elif ask_user == 3:
                    self.premium_listing_handler()
                # message sub menu module
                elif ask_user == 4:
                    self.messages_handler()
                elif ask_user == 5:
                    self.history_handler()
                else:
                    print(Config.LISTING_ERROR_PROMPT)
            except ValueError:
                print(Config.VALUE_ERROR_PROMPT)

    # @handle_exceptions
    def messages_handler(self):
        while True:
            try:
                ask = int(input(Config.MESSAGES_VIEW_PROMPT))
                if ask == int(Config.MESSAGES_VIEW_PROMPT_LENGTH):
                    break
                elif 0 < ask <= len(self.message_menu):
                    self.message_menu[ask]()
                else:
                    print(Config.LISTING_ERROR_PROMPT)
            except ValueError:
                print(Config.VALUE_ERROR_PROMPT)

    def user_handler(self):
        while True:
            try:
                ask = int(input(Config.ADMIN_USER_OPS_MENU))
                if ask == int(Config.ADMIN_USER_OPS_MENU_LENGTH):
                    break
                elif 0 < ask <= len(self.admin_user_menu):
                    self.admin_user_menu[ask]()
                else:
                    print(Config.LISTING_ERROR_PROMPT)
            except ValueError:
                print(Config.VALUE_ERROR_PROMPT)

    def url_handler(self):
        while True:
            try:
                ask = int(input(Config.ADMIN_URL_OPS_MENU))
                if ask == int(Config.ADMIN_URL_OPS_MENU_LENGTH):
                    break
                elif 0 < ask <= len(self.admin_url_menu):
                    self.admin_url_menu[ask]()
                else:
                    print(Config.LISTING_ERROR_PROMPT)
            except ValueError:
                print(Config.VALUE_ERROR_PROMPT)

    def premium_listing_handler(self):
        while True:
            try:
                ask = int(input(Config.ADMIN_PREMIUM_LISTING_OPS_MENU))
                if ask == int(Config.ADMIN_PREMIUM_LISTING_OPS_MENU_LENGTH):
                    break
                elif 0 < ask <= len(self.admin_premiumlisting_menu):
                    self.admin_premiumlisting_menu[ask]()
                else:
                    print(Config.LISTING_ERROR_PROMPT)
            except ValueError:
                print(Config.VALUE_ERROR_PROMPT)

    def history_handler(self):
        while True:
            try:
                ask = int(input(Config.ADMIN_HISTORY_OPS_MENU))
                if ask == int(Config.ADMIN_HISTORY_OPS_MENU_LENGTH):
                    break
                elif 0 < ask <= len(self.admin_history_menu):
                    self.admin_history_menu[ask]()
                else:
                    print(Config.LISTING_ERROR_PROMPT)
            except ValueError:
                print(Config.VALUE_ERROR_PROMPT)
