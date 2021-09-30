from output_module import output
from time_module import get_time
from database import *
from input_module import take_input
from internet import check_internet_connection, check_on_wikipedia
from date import get_date 
import assistant_detail
from web import *
from news_module import get_news
from opencvnew import open_mobile_camera

import os
def process(query):
    answer = get_answer_from_memory(query)
   




    if answer == "get time details":
        return("Time is " + get_time())
    elif answer == "check internet connection":
        if check_internet_connection():
            return "internet is connected"
        else:
            return "internet is not connected"
    elif answer == "open currency converter":
        
        os.system('currency_converter.py')
    elif answer == "on mic":
        
        turn_on_mic
        
    elif answer == "off mic":
        turn_off_mic
        return "mic is off"
    elif answer == "on speech":
        return turn_on_speech()
    elif answer == "off speech":
        return turn_off_speech()
    elif answer == "say your name":
        return "my name is " + get_name()
    elif answer == "open facebook":
        open_facebook()
        return "opening facebook"
    elif answer == "open google":
        open_google()
        return "opening google"
    elif answer == "open ezzy int":
        open_ezzy_int()
        return "opening ezzy international website"
    elif answer == "get news":
        get_news()
    elif answer == "search video":
        output ("please tell me the name of video")
        vid = take_input()
        open_youtube_video(vid)
        output ("ok")
    elif answer == "open android camera":
        open_mobile_camera
        return ("opening mobile camera")
    elif answer == "change name":
        output("okay! what do you wanna call me")
        temp = take_input()
        if temp == assistant_detail.name:
            return "It seems you like my name "
        else:
            update_name(temp)
            assistant_detail.name = temp
            return "now you can call me " + temp
    elif answer =="send whatsapp message":
        output("please tell me number ")
        number = take_input
        output("what is the message")
        message = take_input
        send_message_whatsapp(number, message)
        
    


    if answer == "get todays date":
        return("date is " + str(get_date())) 


    else: 
        output("Don't know this one should I check on internet for you sir?")
        ans = take_input()
        if "yes" in ans:
            answer = check_on_wikipedia(query)
            if answer != "":
                return answer
        else:
            output("I don't know this one, please tell me what it means.")
            ans = take_input()
            if "it means" in ans:
                ans = ans.replace("it means", "")
                ans = ans.strip()
                value = get_answer_from_memory(ans)
                if value == "":
                    return "Can't help with this one "
                else:
                    insert_question_and_answer(query, value)
                    return "Thanks I will remember it for the next time"
            else:
                return "can't help with this one"
            
         
        
        
