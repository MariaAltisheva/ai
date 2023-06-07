# https://pythonprogramminglanguage.com/text-to-speech/
import streamlit as st
import numpy as np
from gtts import gTTS

option = st.selectbox(
    'Выберите язык вашего текста',
    ('ru', 'en'))

st.write('Вы выбрали:', option)



title = st.text_input('Введите текст для озвучивания')
# st.write('The current movie title is', title)

if option and title:
    tts = gTTS(text=title, lang=option)
    tts.save("good.mp3")



    audio_file = open('good.mp3', 'rb')
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format='audio/mp3')

# sample_rate = 44100  # 44100 samples per second
# seconds = 2  # Note duration of 2 seconds
# frequency_la = 440  # Our played note will be 440 Hz
# # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
# t = np.linspace(0, seconds, seconds * sample_rate, False)
# # Generate a 440 Hz sine wave
# note_la = np.sin(frequency_la * t * 2 * np.pi)
#
# st.audio(note_la, sample_rate=sample_rate)