from config.config import Config
from utils.dicts import SubmittedVideo


class SubmittedVideoController:
    def __init__(self, uid):
        self.uid = uid
        self.submit_obj = SubmittedVideo(uid)
        self.submit_menu = self.submit_obj.submit_menu()

    def submitted_video_module(self, transcript, summary, hid):
        while True:
            ask = int(input(Config.AFTER_SUBMITTING_URL_PROMPT))
            if ask == int(Config.AFTER_SUBMITTING_URL_PROMPT_LENGTH):
                print(Config.EXITING_PROMPT)
                return None
                break
            n = len(self.submit_menu)
            if 0 < ask <= n:
                self.submit_menu[ask](transcript, summary, hid)
            else:
                print(Config.INVALID_INPUT_PROMPT)
