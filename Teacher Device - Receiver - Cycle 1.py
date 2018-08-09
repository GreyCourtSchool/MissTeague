from microbit import *
import radio

radio.on()

def updateClass(update):
    display.show(update) #outputs on screen
    print(update) #sends the output up the serial cable

while True:
    update = radio.receive()
    try: #validation to ensure the recieved message has length
        if len(update)>0:
            updateClass(update)
    except:
        pass
    

