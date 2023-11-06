import logging
from database.db_ops.users_db import UsersDB
from config.config import Config
from utils.dicts import PremiumMap
from users.submittedvideo.submitted_video_module import SubmittedVideoController
from utils.exception_handler import handle_exceptions
from config.log_config.log_config import LogStatements
logger = logging.getLogger('premium_user')


class PremiumUser:
    def __init__(self, uid):
        self.uid = uid
        self.user = UsersDB(self.uid)
        self.premium_map = PremiumMap(uid)
        self.premium_menu = self.premium_map.premium_menu()
        self.submitted_video_obj = SubmittedVideoController(uid)

    # @handle_exceptions
    def premium_module(self):
        print(Config.PREMIUM_USER_INTRO)
        while True:
            try:
                ask = int(input(Config.PREMIUM_PROMPT))
                if ask == int(Config.PREMIUM_PROMPT_LENGTH):
                    print(Config.EXITING_PROMPT)
                    logger.info(LogStatements.premium_user_logout)
                    break
                # using dictionary - functionality mapping
                elif 0 < ask <= len(self.premium_menu):
                    res = self.premium_menu[ask]()
                    if res == None:
                        continue
                    if res:
                        # If good video or premium listed video then redirect
                        self.submitted_video_obj.submitted_video_module(res[0], res[1], res[2])
                        continue
                    elif res == False:
                        if ask == 6:
                            logger.info(LogStatements.user_downgraded_to_non_premium)
                            # Role Changing
                            return "premium"
                        break
                    elif res == None:
                        continue
                else:
                    print(Config.INVALID_INPUT_PROMPT)
            except ValueError:
                print("Numbers only")
            return None

