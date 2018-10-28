from guizero import App, PushButton, Window, Text, TextBox, ListBox, error
from DatabaseClassv2 import Database

class GUI(Database): #creates the app within which all others are defined
   def __init__(self,width, height, title, bg):
      self.bg = bg
      self.app = App(title=title,width=width,height=height,bg = self.bg)
      self.contents = []
      self.users = []
      with open("users.txt","r") as self.file:
         for line in self.file:
            self.contents.append(line.split(","))
      self.text = Text(self.app,"Select a user below", grid=[0,0,3,1])#add in font size
      for entry in range(len(self.contents)):
         self.users.append(self.contents[entry][0])
      self.users.append("New User...")
      self.selectUser = ListBox(self.app, items=self.users,command=self.selectUser,scrollbar=True)
      self.button = PushButton(self.app,text="Cancel",command=self.close)

   def selectUser(self,value):
      if value == "New User...":
         self.newUser()
      else:
         value = value.replace(" ","")
         self.openUser(value+".db")
         with open("users.txt","a") as self.file:
            self.file.wrie(value)

   def newUser(self):
      print("new user")
      self.app.hide()
      self.window = Window(self.app,"Create new user",height=100, width=200,bg = self.bg)
      self.text =Text(self.window,text="Enter the your name\nE.g. Mr Hirst", size=9)
      self.entry = TextBox(self.window,width=10)
      self.button = PushButton(self.window,text="Submit",command=self.submitNewUser)

   def submitNewUser(self):
      self.user = self.entry.get()
      if self.user.isalpha() or " " in self.user or "-" in self.user:
         self.user = self.user.replace(" ","")
         self.openUser(self.user)
         self.generateDatabase()
         print("new database created")
      else:
         error("Input Error","You must only include letters, a space or hyphen")

   def close(self):
      self.app.destroy()
      quit()

   def choice(self):
      pass

   def selectClass(self):
      pass

   def runClass(self):
      pass

   def analyticsHome(self):
      pass

   def setup(self):
      pass

