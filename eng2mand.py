import pyttsx3
from playsound import playsound
import gtts
import os
from 汉字 import 汉语拼音
from 翻译 import 英语

def english_to_chinese():
    user_input = input("Enter a word in English:")
    value = 英语(user_input, 'en', 'zh')
    汉语拼音(value)