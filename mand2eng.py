import pyttsx3
from playsound import playsound
import gtts
import os
from 汉字 import 汉语拼音
from 翻译 import 英语

def chinese_to_english(user_input):
    user_input = str(user_input)
    language = 'zh'
    # zh is Mandarin Chinese
    汉语拼音(user_input)
    return 英语(user_input,'zh','en')
    gtts.gTTS(text=user_input, lang=language, slow=True).save("output.mp3")
