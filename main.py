from eng2mand import english_to_chinese
from mand2eng import chinese_to_english


# basic logic to ask the question until you get a valid response.
while True:
    user_inp = str(input("english to chinese test: "))
    if user_inp == "english":
        english_to_chinese()
        break
    if user_inp == "chinese":
        chinese_to_english()
        break
    