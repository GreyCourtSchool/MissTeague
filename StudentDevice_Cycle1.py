from microbit import *
import radio

#assignment of key data structures
microID = "1"
state = "R"
scrollState = ["R","A","Y","G"]
scrollIndex = 0

radio.on()
#on method from radio record

while True:
    display.show(microID)
    gesture = accelerometer.current_gesture() 
    #this method access the current gesture to be used to determine the next condition
    
    if gesture == 'face down':
        display.show(state)
        while True:
            
            #scrolling between states section
            if button_a.was_pressed():
                scrollIndex += 1
                if scrollIndex == 4: #validation to ensure index remains between 0 and 3
                    scrollIndex = 0
                display.show(scrollState[scrollIndex]) #visual feedback on the state changes to the user
               
            #sending the signal section
            if button_b.was_pressed():
                state = scrollState[scrollIndex]
                display.show(state) #visual confirmation of current state
                radio.send(microID+','+state)
