# streamlit interface 
import streamlit as st
from pypinyin import pinyin
from translate import Translator
    
st.title("English to Chinese and Chinese to English")

# create an input box for the user to enter the text to be translated.
user_input = st.text_input("Enter the text to be translated:")

eng_to_pinyin = st.button("English to Pinyin")

if eng_to_pinyin:
    # translate user input into mandarin, using the translate module
    translator = Translator(to_lang="zh")
    translation = translator.translate(user_input)
    st.write(translation)

    pis = pinyin(translation, heteronym=True)
    for i in range(len(pis)):
        st.write(pis[i])  # print the pinyin characters one by one