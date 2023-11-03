import googletrans
import os
import json
from googletrans import Translator

class Translator_handler:
    def __init__(self):
        pass

    def translate(self, content, target):
        translator = Translator()
        result = translator.translate(content, dest=target)
        return result

