from gtts import gTTS
from playsound import playsound
import random
def speak(text):
    r1 = random.randint(1,10000000)
    r2 = random.randint(1,10000000)

    speech = str(r2)+"randomtext"+str(r1) +".mp3"
    tts = gTTS(text)
    tts.save(speech)
    playsound(speech)
               
