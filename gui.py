# streamlit interface 
import streamlit as st
from main import main
from eng2mand import english_to_chinese
from mand2eng import chinese_to_english


st.title("English to Chinese and Chinese to English")

# create an input box for the user to enter the text to be translated.
user_input = st.text_input("Enter the text to be translated:")
buttonclick = st.button("English to Pinyin")

if buttonclick:
    st.write(main(user_input,"english"))
    st.audio("output.mp3")
    
