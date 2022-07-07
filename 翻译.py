from translate import Translator
def 英语(user_input, lang_from, lang_to):
    translator = Translator(from_lang=lang_from, to_lang=lang_to)
    translation = translator.translate(user_input)
    print(translation)
    return translation