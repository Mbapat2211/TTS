import pyttsx3 as pt
import streamlit as st
import os

os.environ['SDL_AUDIODRIVER'] = 'dsp'

st.title("Text to Speech Converter")

text = st.text_input("Enter the text here")
submit = st.button("Convert to Speech")

if submit:

    speak = pt.init()
    speak.say(text)
    speak.runAndWait()
    speak.stop()
