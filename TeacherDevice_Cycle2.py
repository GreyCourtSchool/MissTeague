import serial
from sense_hat import SenseHat
import datetime
import sqlite3

def setClassroom(classroom,sense):
  sense.clear() #clears the screen of any coloured pixels
  for key in classroom:
    sense.set_pixel(classroom[key][0],classroom[key][1],(0, 0, 255))
    
def generateDatabase():
    database = "SRAYGS.db" #this is the value that is returned when this subroutine is called
    with sqlite3.connect(database)as db:
        cursor = db.cursor()
        #used if not exists instead of selection statement 
        sql  = """CREATE Table IF NOT EXISTS classroomTable(
                roomName text PRIMARY KEY,
                student1 text, student2 text, student3 text, student4 text, student5 text, student6 text, student7 text,
                student8 text, student9 text, student10 text, student11 text, student12 text, student13 text, 
                student14 text, student15 text,student16 text, student17 text, student18 text, student19 text, 
                student20 text, student21 text, student22 text, student23 text, student24 text, student25 text, 
                student26 text, student27 text, student28 text, student29 text, student30 text, student31 text, 
                student32 text);
                """
        cursor.execute(sql)

        sql = """ CREATE Table IF NOT EXISTS yearsTable(
                yearID integer PRIMARY KEY AUTOINCREMENT,
                academicYear text); """
        cursor.execute(sql)
        
        sql = """ CREATE Table IF NOT EXISTS classesTable(
                classID integer PRIMARY KEY AUTOINCREMENT,
                yearID integer NOT NULL,
                roomName text NOT NULL,
                className text,
                FOREIGN KEY (roomName) REFERENCES classroomTable(roomName),
                FOREIGN KEY (yearID) REFERENCES yearsTable(yearID)); """
        cursor.execute(sql)

        sql = """ CREATE Table IF NOT EXISTS lessonTable(
               lessonID integer PRIMARY KEY AUTOINCREMENT,
               roomName text NOT NULL,
               deviceID integer,
               date text,
               time text,
               currentState text,
               FOREIGN KEY (roomName) REFERENCES classroomTable(roomName)); """
        cursor.execute(sql)
        
        return database #return statement used to call the database in other subroutines

def setClass():
    database = generateDatabase()
    
    with sqlite3.connect(database)as db:
        cursor = db.cursor()
        sql  = "SELECT className FROM classesTable"
        cursor.execute(sql)
        print("***Existing Classes***")
        result = cursor.fetchall()
        for each in result:
            print(" - " + each[0])
        print("From the list above, type the class you want to choose")
        currentClass = input(">")
       
        #setting class
        result = getClass(database,currentClass)
        if result:
            print(result[0][0])
        else:
            print("Your new class will now be added")
            sql = "INSERT INTO classesTable VALUES (null,0,\"T1\",\"{}\")".format(currentClass.lower())
            cursor.execute(sql)
            currentClass=getClass(database,currentClass)

def getClass(database,currentClass):
    with sqlite3.connect(database)as db:
        cursor = db.cursor()
        sql = "SELECT classID FROM classesTable WHERE className = \"{}\"".format(currentClass.lower())
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

            
def writeSQL():
     with sqlite3.connect("SRAYGS.db") as db:
        cursor = db.cursor()
        sql  = input()
        cursor.execute(sql)
        result = cursor.fetchall()
        for each in result:
            print(each)


def radioRecieve(sense,studentStates,classroom):
  
  #setup of the serial connections
  PORT = "/dev/ttyACM4" #USB port that the reciever Micro:bit is connected to - ls /dev/ttyA*
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
      return changeState(sense,studentUpdate,studentStates,classroom)
  except ValueError:
      print("Invalid ID recieved") #if the ID cannot be changed to an integer this message shows on console
  except IndexError:
      print("Invalid state recieved") #if the studentUpdate doesn't have an index 1 this error will show on the console
      

def changeState(sense,studentUpdate,studentStates,classroom):
  
  #colours dict {"key": (R,G,B)}
  colours = {"R":(255,0,0),"A":(255,165,0),"Y":(255,255,0),"G":(0,255,0)}

  #set_pixel(x,y,(r,g,b))
  sense.set_pixel(classroom[studentUpdate[0]][0],classroom[studentUpdate[0]][1],colours[studentUpdate[1]]) #updates the pixel
  studentStates[int(studentUpdate[0])-1] = studentUpdate[1] #updates the states list with the new student state
  print(studentStates) #not essential - used for testing to show the updated list of studentStates

  with sqlite3.connect("SRAYGS.db")as db:
        cursor = db.cursor()
        #used if not exists instead of selection statement 
        #attribues - lessonID, roomName,deviceID integer,date text, time text, currentState text
        date = str(datetime.date.today().strftime("%d/%m/%y"))
        time = str(datetime.datetime.today().strftime("%H%M"))
        sql  = "INSERT INTO lessonTable VALUES (null,\'{}\',\'{}\',\'{}\',\'{}\',\'{}\');"
                                                                        .format("T1",studentUpdate[0],date,time,studentUpdate[1])
        print(sql)
        cursor.execute(sql)

  return studentStates #this is inplace of using studentState as a global variable
  
  
sense = SenseHat()

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

#main program starts here
setClassroom(classroom,sense)
generateDatabase()
setClass()
while True:
    studentStates = radioRecieve(sense,studentStates,classroom) 
    #keeps student states updated in the mina program to avoid global variables
