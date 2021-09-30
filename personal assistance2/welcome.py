from time_module import get_hours
from output_module import output
import database 
def greet():
    hour = int(get_hours())
    
    previous_date = ""
    today_date = ""
    
    if previous_date == today_date:
       output("Welcome back sir")
    else:
        hour = int(get_hours())
        
    if hour >=6 and hour < 12:
        return("Good Morning, sir ")
    
    elif hour >= 12 and hour < 16:
        output("Good After noon, sir")
    else:
        output("Good Evenning, sir")
         

     

     
     
