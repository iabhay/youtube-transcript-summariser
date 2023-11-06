import logging
from database.db_ops.users_db import UsersDB
from config.config import Config
from utils.dicts import NonPremiumMap
from users.submittedvideo.submitted_video_module import SubmittedVideoController
from users.premium_user.premium_user import PremiumUser
from utils.exception_handler import handle_exceptions
from config.log_config.log_config import LogStatements
logger = logging.getLogger('non_premium_user')

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
            try:
                # using dictionary - functional mapping
                ask = int(input(Config.NON_PREMIUM_PROMPT))
                n = int(Config.NON_PREMIUM_PROMPT_LENGTH)
                if ask == n:
                    logger.info(LogStatements.non_premium_user_logout)
                    print(Config.EXITING_PROMPT)
                    break
                elif 0 < ask <= len(self.non_premium_menu):
                    res = self.non_premium_menu[ask]()
                    if res == None:
                        continue
                    elif res:
                        # if video is good content then redirect to submitted video functionalities
                        self.submitted_video_obj.submitted_video_module(res[0], res[1], res[2])
                        continue
                    elif res == False:
                        # Role changing
                        if ask == 2:
                            logger.info(LogStatements.user_upgraded_to_premium)
                            return "nonpremium"
                        break
                    elif res == None:
                        continue
                else:
                    print(Config.INVALID_INPUT_PROMPT)
                    continue
            except ValueError:
                print("Numbers only")
            return None
