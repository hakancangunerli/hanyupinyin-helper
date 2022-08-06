import pyttsx3
from playsound import playsound
import gtts
import os
from 汉字 import 汉语拼音
from 翻译 import 英语

def english_to_chinese(user_input):
    user_input = str(user_input)
    value = 英语(user_input, 'en', 'zh')
    return 汉语拼音(value)