# $ pip install pypinyin
from pypinyin import pinyin 
# import text to speech 
import pyttsx3
from playsound import playsound
import gtts
import os

user_input = input("Enter a word in Mandarin:")

# zh is Mandarin 
print(pinyin(user_input))

# actually say the word using gtts 

language = 'zh'
myobj = gtts.gTTS(text=user_input, lang=language, slow=True)
myobj.save("test.mp3")