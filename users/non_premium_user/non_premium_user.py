from database.db_ops.users_db import UsersDB
from config.config import Config
from users.premium_user.premium_user import PremiumUser
from utils.dicts import NonPremiumMap
from users.submittedvideo.submitted_video_module import SubmittedVideoController


class NonPremiumUser:
    def __init__(self, uid):
        self.uid = uid
        self.user = UsersDB(self.uid)
        self.premium_user = PremiumUser(self.uid)
        self.non_premium_map = NonPremiumMap(uid)
        self.non_premium_menu = self.non_premium_map.non_premium_menu()
        self.submitted_video_obj = SubmittedVideoController(uid)

    # @handle_exceptions
    def non_premium_module(self):
        print(Config.BASIC_USER_INTRO)
        while True:
            ask = int(input(Config.NON_PREMIUM_PROMPT))
            n = int(Config.NON_PREMIUM_PROMPT_LENGTH)
            if ask == n:
                print(Config.EXITING_PROMPT)
                break
            elif 0 < ask <= len(self.non_premium_menu):
                res = self.non_premium_menu[ask]()
                if res:
                    self.submitted_video_obj.submitted_video_module(res)
                elif res == False:
                    break
            else:
                print(Config.INVALID_INPUT_PROMPT)
