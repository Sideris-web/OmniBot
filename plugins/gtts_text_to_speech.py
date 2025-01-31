from gtts import gTTS
import os

class GTTSTextToSpeech:
    @staticmethod
    def text_to_speech(text, lang="en"):
        tts = gTTS(text=text, lang=lang)
        filename = "output.mp3"
        tts.save(filename)
        return filename
