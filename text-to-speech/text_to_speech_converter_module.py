from gtts import gTTS
import os


def text_to_speech(text, language='en'):
    # en (get all language codes from google search: google speech language codes
    output = gTTS(text=text, lang=language, slow=False)
    output.save('output.mp3')

    # open a program in operating system
    # start = start play
    os.system("start output.mp3")
