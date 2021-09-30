import webbrowser
import datetime
import pywhatkit as whatsapp
def open_facebook():
    webbrowser.open("http://facebook.com")
def open_google():
    webbrowser.open("http://google.com")
def open_ezzy_int():
    webbrowser.open("https://ezzyint.com")
def open_youtube_video(ytv):
    webbrowser.open("https://www.youtube.com/results?search_query="+ytv)
def send_message_whatsapp():
    x=datetime.datetime.now(+number,message)
    whatsapp.sendwhatmsg(+number,message,x.strftime("%H"),x.strftime("%M"))
