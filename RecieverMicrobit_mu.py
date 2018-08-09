from microbit import *
import radio

radio.on()
def updateClass(update):
    studentUpdate = update.split(",")
   # if classState[studentUpdate[0]] != studentUpdate[1]:
    display.show(update)
    print(update)

#classState = ["G"*30]

while True:
    update = radio.receive()
    try:
        if len(update)>0:
            updateClass(update)
    except:
        pass
    

