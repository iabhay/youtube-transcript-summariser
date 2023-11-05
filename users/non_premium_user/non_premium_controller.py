# from config.config import Config
#
# class NonPremiumUserController:
#     def __init__(self, uid):
#         self.uid = uid
#         self.submit_obj = SubmittedVideo(uid)
#
#     def non_premium_module(self):
#         while True:
#             ask = int(input(Config.AFTER_SUBMITTING_URL_PROMPT))
#             if ask == int(Config.AFTER_SUBMITTING_URL_PROMPT_LENGTH):
#                 print(Config.EXITING_PROMPT)
#                 break
#             n = len(self.submit_obj.submit_menu())
#             if 0 < ask <= n:
#                 self.submit_obj.submit_menu()[ask]()
#             else:
#                 print(Config.INVALID_INPUT_PROMPT)
