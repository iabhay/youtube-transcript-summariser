from users.users_helper import UsersHelper
from users.premium_user.premium_user_controller import PremiumUserController
from users.submittedvideo.submit_video_ops import SubmitVideoOps
class NonPremiumMap:
    def __init__(self, uid):
        self.user_helper = UsersHelper(uid)
        self.submit_video = SubmitVideoOps(uid)

    def non_premium_menu(self):
        non_premium_dict = {
            1: self.submit_video.submit_video,
            2: self.user_helper.upgrade_to_premium
        }
        return non_premium_dict


class PremiumMap:
    def __init__(self, uid):
        self.user_helper = UsersHelper(uid)
        self.premium_controller = PremiumUserController(uid)
        self.submit_video = SubmitVideoOps(uid)

    def premium_menu(self):
        premium_dict = {
            1: self.submit_video.submit_video,
            2: self.premium_controller.send_message_to_admin,
            3: self.premium_controller.premium_listing_of_banned_url,
            4: self.premium_controller.view_my_history,
            5: self.user_helper.downgrade_to_basic
        }
        return premium_dict


class SubmittedVideo:
    def __init__(self, uid):
        self.user_helper = UsersHelper(uid)
        self.submit_video = SubmitVideoOps(uid)

    def submit_menu(self):
        submit_dict = {
            1: self.submit_video.save_summary,
            2: self.submit_video.save_transcript,
            3: self.submit_video.show_video_details
        }
        return submit_dict
