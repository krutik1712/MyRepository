import eel
from playsound import playsound

# Playing assiatnt sound function

@eel.expose
def playEosSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)