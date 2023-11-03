import yt_dlp
import time
import re
import os
from pydub import AudioSegment
import speech_recognition as sr
import math
from tqdm import tqdm
from googletrans import Translator

url = "https://www.youtube.com/watch?v=xbQkVXU5ELY"

ydl_opts={}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
video_title = info_dict['title']
video_name = re.sub('[\\\\/*?:"<>|]', '', video_title)
name = video_name
ydl_opts = {
     'format': 'm4a/bestaudio/best',
         'noplaylist': True,
         'continue_dl': True,
         'outtmpl': f'./{name}.wav',
         'postprocessors': [{
             'key': 'FFmpegExtractAudio',
             'preferredcodec': 'wav',
             'preferredquality': '192',
         }],
         'geobypass':True,
         'ffmpeg_location':'/usr/bin/ffmpeg'
 }

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
     error_code = ydl.download(url)


class SplitWavAudioMubin():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + filename
        self.audio = AudioSegment.from_wav(self.filepath)

    def get_duration(self):
        return self.audio.duration_seconds

    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(split_filename, format="wav")

    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 60)
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i + min_per_split, split_fn)
            if i == total_mins - min_per_split:
                print('All splited successfully')
        print('>>> Video duration: ' + str(self.get_duration()))


def split_audio(file_name):
    directory = "splitted files for: " + file_name
    os.mkdir(directory)
    os.chdir(directory)
    split_wav = SplitWavAudioMubin("../", file_name)
    split_wav.multiple_split(min_per_split=1)

file_name = "{}.wav".format(video_name)
split_audio(file_name)

search_dir = "./"
files = filter(os.path.isfile, os.listdir(search_dir))
files = [os.path.join(search_dir, f) for f in files] # add path to each file
files.sort(key=lambda x: os.path.getmtime(x))
files

texts = []
recognizer = sr.Recognizer()

for file in tqdm(files):
    with sr.AudioFile(file) as source:
        recorded_audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(
                recorded_audio,
                language="en-US" ## Replace with language keyword
            )
        texts.append(text)
    except Exception as ex:
        print(ex)

result = ""
for text in texts:
    result += " " + text

os.chdir("../")
text_file = open("Transcription_"+ file_name[:-4] +".txt", "w")
text_file.write(result)
text_file.close()

translator = Translator()

translate_text = ""
for text in texts:
    translate_text += " " + translator.translate(text, dest='fr').text
print(translate_text)


text_file = open("Transcription_translated_"+ file_name[:-4] +".txt", "w")
text_file.write(translate_text)
text_file.close()

from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

ARTICLE = result
summary_text = summarizer(ARTICLE, max_length=100, min_length=int(len(result.split(" "))/10), do_sample=False)[0]["summary_text"]
print(summary_text)