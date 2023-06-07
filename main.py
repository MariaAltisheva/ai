from gtts import gTTS
import os
# tts = gTTS(text='Good morning', lang='en')
tts = gTTS(text='Доброе утро', lang='ru')
tts.save("good.mp3")
# os.system("mpg321 good.mp3")