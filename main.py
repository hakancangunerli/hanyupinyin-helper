from eng2mand import english_to_chinese
from mand2eng import chinese_to_english

def main(user_input_text, language):
    # basic logic to ask the question until you get a valid response.
    while True:
        user_inp = str(user_input_text)
        if language == "english":
            return english_to_chinese(user_inp)
            break
        if language == "chinese":
            return chinese_to_english(user_inp)
            break 