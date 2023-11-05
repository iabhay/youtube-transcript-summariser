from service_handler.transcript_handler.transcript_generator import transcriptor
from service_handler.content_checker.content_check import ContentChecker
from database.db_ops.ban_url_db import BanUrlDB
from database.db_ops.searches_db import SearchesDB
from database.db_ops.history_db import HistoryDB
from config.config import Config
from database.db_ops.premium_listing_db import PremiumListingsDB
from service_handler.summary_handler.sum_gen import SummaryGenerator


class SubmitVideoOps:
    def __init__(self, uid):
        self.uid = uid
        self.transcript_obj = transcriptor()
        self.content_check_obj = ContentChecker()
        self.ban_url_obj = BanUrlDB()
        self.search_count_db = SearchesDB(self.uid)
        self.summary = ""
        self.summary_obj = SummaryGenerator()
        self.urlid = ""
        self.history_obj = HistoryDB(self.uid)
        self.transcript = ""

    def submit_video(self):
        ask = input(Config.SUBMIT_VIDEO_PROMPT)
        if ask != "1":
            print("Processing...")
            self.urlid = self.transcript_obj.extract_video_id(ask)
            valid = self.ban_url_obj.fetch_ban_url(self.urlid)
            premium_list_obj = PremiumListingsDB(self.uid)
            check_premium_lisiting = premium_list_obj.check_premium_list_url(self.urlid)
            if valid and check_premium_lisiting == None:
                print("Already Banned Url")
            else:
                self.transcript = self.transcript_obj.format_transcript(self.urlid)
                summary = self.summary_obj.summary_generator(self.transcript)
                # print(self.transcript)
                if self.transcript:
                    hid = self.history_obj.save_history(self.urlid)
                    if check_premium_lisiting is None:
                        content_check = self.content_check_obj.analyze_text(self.transcript)
                        if content_check:
                            for key, value in content_check.items():
                                if content_check[key] > 0:
                                    self.ban_url_obj.save_ban_url(self.urlid, key, value)
                                    if not self.search_count_db.update_user_search_count(3):
                                        return False
                                    break
                    return [self.transcript, summary, hid]
                else:
                    print("This video is not supported. Please try other videos.")
                    return None
        return None

    def save_summary(self, transcript, summary, hid):
        with open(f"downloadable_results/summary_outputs/{hid}_summary.txt", "w") as f:
            f.write(summary)
        print("Summary File Generated")

    def save_transcript(self, transcript, summary, hid):
        with open(f"downloadable_results/transcript_outputs/{hid}_transcript.txt", "w") as f:
            f.write(transcript)
        print("Transcript File Generated")


    def show_video_details(self, transcript, summary, hid):
        read_transcript = transcript
        read_summary = summary
        transcript_word = read_transcript.split()
        summary_word = read_summary.split()
        print(f"Video URLID - {hid}\nTranscript Length - {len(transcript_word)}\nSummary Length - {len(summary_word)}")

