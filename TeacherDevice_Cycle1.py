import serial
from sense_hat import SenseHat

def setClassroom(classroom,sense,colours):
  
  sense.clear() #clears the screen of any coloured pixels
  for key,value in classroom:
    sense.set_pixel(classroom[key][0],classroom[key][1],(0, 0, 255))

def radioRecieve(sense):
  
  #setup of the serial connections
  PORT = "/dev/ttyACM1" #USB port that the reciever Micro:bit is connected to - ls /dev/ttyA*
  BAUD = 115200 #bits per second
  s = serial.Serial(PORT)
  s.baudrate = BAUD
  s.parity   = serial.PARITY_NONE
  s.databits = serial.EIGHTBITS
  s.stopbits = serial.STOPBITS_ONE

  #Data being readin from the serial connection
  data = s.readline().decode('UTF-8') #UTF-8 is a method of unicode endcoding that microbits use for serial connections
  data = data.rstrip() #removes any bits that aren't the data
  print(data) #not essential - used for testing to output to shell the recieved data
  
  studentUpdate = ""
  studentUpdate = data.split(",") #data is packaged with a , to differenitate between the ID and state - splits to a list
 
  #validation against invalid recieved messages
  try:
      int(studentUpdate[0]) #validation to check the ID is a number
      if studentUpdate[1] not in ["R","A","Y","G"]: #validation to check state is in valid range
          print("Invalid state recieved")
      return changeState(sense,studentUpdate)
  except ValueError:
      print("Invalid ID recieved") #if the ID cannot be changed to an integer this message shows on console
  except IndexError:
      print("Invalid state recieved") #if the studentUpdate doesn't have an index 1 this error will show on the console
      

def changeState(sense,studentUpdate,studentStates):
  
  #colours dict {"key": (R,G,B)}
  colours = {"R":(255,0,0),"A":(255,165,0),"Y":(255,255,0),"G":(0,255,0)}

  #classroom dict {"key":(x,y)}
  classroom = {"1":(0,1),"2":(0,2),"3":(0,3),"4":(0,4),"5":(0,5),"6":(0,6),"7":(0,7),
             "8":(3,7),"9":(3,6),"10":(3,5), "11":(3,4), "12":(3,3), "13":(3,2), "14":(3,1),"15":(3,0),
             "16":(4,0),"17":(4,1),"18":(4,2),"19":(4,3),"20":(4,4),"21":(4,5),"22":(4,6),"23":(4,7),
             "24":(7,7),"25":(7,6),"26":(7,5),"27":(7,4),"28":(7,3),"29":(7,2),"30":(7,1),"31":(7,0)}
 
  #set_pixel(x,y,(r,g,b))
  sense.set_pixel(classroom[studentUpdate[0]][0],classroom[studentUpdate[0]][1],colours[studentUpdate[1]]) #updates the pixel
  studentStates[int(studentUpdate[0])-1] = studentUpdate[1] #updates the states list with the new student state
  print(studentStates) #not essential - used for testing to show the updated list of studentStates
  return studentStates #this is inplace of using studentState as a global variable
  
  
  
sense = SenseHat()

#Uses the ID read in from the serial connection on the attached microbit
studentStates = ["G","G","G","G","G","G","G",
                 "G","G","G","G","G","G","G","G",
                 "G","G","G","G","G","G","G","G",
                 "G","G","G","G","G","G","G","G"]

setClassroom(classroom,sense)
while True:
  #validation against the serial connection being removed
  try:
    studentStates = radioRecieve(sense)
  except SerialError:
    s.close() #closes the serial connection
