import os
import pyttsx3 as tts

greeting = "Welcome to my app"
print(greeting)
tts.speak(greeting)

choices = [
    'Press 1 for Google Chrome',
    'Press 2 for Discord',
    'Press 3 for Notepad',
    'Press 4 for VLC Player'
]

for s in choices:
    print(s)

print("Enter your choice: ", end="")
c = int(input())

if c == 1:
    os.system('google-chrome')
elif c == 2:
    os.system('discord')
elif c == 3:
    os.system('gedit')
elif c == 4:
    os.system('vlc')
else:
    print('Wrong choice')

tts.speak('Thanks for using me.')