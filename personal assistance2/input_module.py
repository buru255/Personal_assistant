import speech_recognition as sr
from database import mic_is_on

def take_input():
    if mic_is_on():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Ready...')
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
        try:
            i = r.recognize_google(audio).lower()
            print('You said: ' + i + '\n')
        except sr.UnknownValueError:
            print('your last command couldn\'t be heard ')
            i = take_input()
        return i
    else:
        i=input("Me: ")
        return i
    
              
    
    
   
