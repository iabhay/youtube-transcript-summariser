from service_handler.transcript_handler.transcript_generator import transcriptor
from service_handler.summary_handler.summary_generator import Summariser
from database.db_ops.users_db import UsersDB
from config.config import Config
from service_handler.content_checker.content_check import ContentChecker
from database.db_ops.ban_url_db import BanUrlDB
# from users.premium_user.premium_user_controller import PremiumUserController
from database.db_ops.searches_db import SearchesDB
# from users.non_premium_user.non_premium_controller import NonPremiumUserController
from utils.dicts import PremiumMap
from users.submittedvideo.submitted_video_module import SubmittedVideoController
class PremiumUser:
    def __init__(self, uid):
        self.uid = uid
        self.user = UsersDB(self.uid)
        self.premium_map = PremiumMap(uid)
        self.premium_menu = self.premium_map.premium_menu()
        self.submitted_video_obj = SubmittedVideoController(uid)
    #
    def premium_module(self):
        print(Config.PREMIUM_USER_INTRO)
        while True:
            ask = int(input(Config.PREMIUM_PROMPT))
            if ask == int(Config.PREMIUM_PROMPT_LENGTH):
                print(Config.EXITING_PROMPT)
                break
            elif 0 < ask <= len(self.premium_menu):
                res = self.premium_menu[ask]()
                if res:
                    self.submitted_video_obj.submitted_video_module(res)
                elif res == False:
                    break
            else:
                print(Config.INVALID_INPUT_PROMPT)

