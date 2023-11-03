from config.config import Config
from transcript_handler.transcript_generator import transcriptor
from content_checker.content_check import ContentChecker
from database.db_ops.ban_url_db import BanUrlDB
from database.db_ops.searches_db import SearchesDB
from summary_handler.summary_generator import Summariser
from database.db_ops.history_db import HistoryDB
from database.db_ops.users_db import UsersDB

class NonPremiumUserController:
    def __init__(self, uid):
        self.uid = uid
        self.transcript_obj = transcriptor()
        self.content_check_obj = ContentChecker()
        self.ban_url_obj = BanUrlDB()
        self.search_count_db = SearchesDB(self.uid)
        self.summary = ""
        self.summary_obj = Summariser()
        self.urlid = ""
        self.history_obj = HistoryDB(self.uid)
        self.transcript = ""

    def non_premium_module(self):
        while True:
            ask = int(input(Config.AFTER_SUBMITTING_URL_PROMPT))
            if ask == 1:
                self.save_summary()
            elif ask == 2:
                self.save_transcript()
            elif ask == 3:
                self.show_video_details()
            elif ask == 4:
                print(f"Exiting!!")
                break
            else:
                print("Please Select Carefully!")

    def submit_video(self, uid):
        ask = input(Config.SUBMIT_VIDEO_PROMPT)
        if ask == "1":
            return "1"
        self.urlid = self.transcript_obj.extract_video_id(ask)
        valid = self.ban_url_obj.fetch_ban_url(self.urlid)
        if valid:
            print("Already Banned Url")
            return False
        else:
            self.transcript = self.transcript_obj.format_transcript(self.urlid)
            if self.transcript:
                self.history_obj.save_history(self.urlid)
                print(self.transcript)
                # self.summary = self.summary_obj.sample_extractive_summarization(self.transcript)
                content_check = self.content_check_obj.analyze_text(self.transcript)
                if content_check:
                    for key, value in content_check.items():
                        if content_check[key] > 0:
                            self.ban_url_obj.save_ban_url(self.urlid, key, value)
                            users_db_obj = UsersDB(uid)
                            ent = users_db_obj.fetch_user_details(uid)
                            role = ent[0][1]
                            if not self.search_count_db.update_user_search_count(3 if role == "nonpremiumuser" else 5):
                                return "Logout"
                            return False
                    return True
            else:
                print("This video is not supported. Please try other videos.")
                return False

    def save_summary(self):
        with open(f"{self.uid}_summary.txt", "w") as f:
            f.write(self.transcript)
        print("Summary File Generated")

    def save_transcript(self):
        with open(f"{self.uid}_transcript.txt", "w") as f:
            f.write(self.transcript)
        print("Transcript File Generated")

    def show_video_details(self):
        read_transcript = self.transcript
        read_summary = self.transcript
        transcript_word = read_transcript.split()
        summary_word = read_summary.split()
        print(f"Video URLID - {self.urlid}\nTranscript Length - {len(transcript_word)}\nSummary Length - {len(summary_word)}")
