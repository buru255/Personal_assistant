from assistant_detail import name
from speak_module import speak
from database import speak_is_on
def output(o):
    if speak_is_on():
        speak(o)

    print(name+ ":" +o)
    print()
