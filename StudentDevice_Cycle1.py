from microbit import *
import radio

microID = "1"
radio.on()

state = "R"
scrollState = ["R","A","Y","G"]

while True:
    display.show(microID)
    gesture = accelerometer.current_gesture()
    if gesture == 'face down':
        display.show(state)
        scrollIndex = 0
        while True:
            change = False
            if button_a.was_pressed():
                scrollIndex += 1
                if scrollIndex == 4:
                    scrollIndex = 0
                display.show(scrollState[scrollIndex])
            if button_b.was_pressed() and change == False:
                if scrollState[scrollIndex] != state:
                    state = scrollState[scrollIndex]
                    change = True
                display.show(state)
                radio.send(microID+','+state)
