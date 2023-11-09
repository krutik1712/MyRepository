import os
import eel
from engine.features import *

eel.init("www")

playEosSound()

# os.system('start chrome --app="http://127.0.0.1:5500/www/index.html"')
os.system('start msedge.exe --app="http://localhost:8000/index.html"')

# eel.start('index.html', mode=None, host='127.0.0.1', block=True)
eel.start('index.html', mode=None, host='localhost', block=True)