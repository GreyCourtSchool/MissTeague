import serial
from sense_hat import SenseHat

def setClassroom(classroom,sense):
  sense.clear()
  for seat in classroom:
    sense.set_pixel(classroom[0],classroom[1],(0, 0, 255))


sense = SenseHat()

PORT = "/dev/ttyACM1" #may need to change this.  ls /dev/ttyA*
BAUD = 115200 #bits per second

s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

studentUpdate = ""
#colours dict {"key": (R,G,B)}
colours = {"R":(255,0,0),"A":(255,165,0),"Y":(255,255,0),"G":(0,255,0)}

#classroom dict {"key":(x,y)}
classroom = {"1":(0,1),"2":(0,2),"3":(0,3),"4":(0,4),"5":(0,5),"6":(0,6),"7":(0,7),
             "8":(3,7),"9":(3,6),"10":(3,5), "11":(3,4), "12":(3,3), "13":(3,2), "14":(3,1),"15":(3,0),
             "16":(4,0),"17":(4,1),"18":(4,2),"19":(4,3),"20":(4,4),"21":(4,5),"22":(4,6),"23":(4,7),
             "24":(7,7),"25":(7,6),"26":(7,5),"27":(7,4),"28":(7,3),"29":(7,2),"30":(7,1),"31":(7,0)}

#Uses the ID read in from the serial connection on the attached microbit
studentStates = ["G","G","G","G","G","G","G",
                 "G","G","G","G","G","G","G","G",
                 "G","G","G","G","G","G","G","G",
                 "G","G","G","G","G","G","G","G"]

setClassroom(classroom,sense)
while True:
    data = s.readline().decode('UTF-8')
    data = data.rstrip()
    print(data) #not essential - used for testing
    studentUpdate = data.split(",")
    print(studentUpdate) #not essential - used for testing
    
    #validation against invalid recieved messaged
    try:
        int(studentUpdate[0])
        if studentUpdate[1] not in ["R","A","Y","G"]:
            print("Invalid state recieved")
        sense.set_pixel(classroom[studentUpdate[0]][0],classroom[studentUpdate[0]][1],colours[studentUpdate[1]]) #updates the pixel
        studentStates[int(studentUpdate[0])-1] = studentUpdate[1] #updates the states list with the new student state
        print(studentStates) #not essential - used for testing
    except ValueError:
        print("Invalid ID recieved")
    except IndexError:
        print("Invalid state recieved")
    
s.close()
