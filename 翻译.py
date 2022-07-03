from translate import Translator
def 英语(user_input):
    translator = Translator(from_lang="zh", to_lang="en")
    translation = translator.translate(user_input)
    print(translation)