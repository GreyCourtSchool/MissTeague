from guizero import App, PushButton, Window, Text, TextBox
from DatabaseClassv2 import Database
'''
class GUI:
   def __init__(self,width, height, title):
      self.app = App(title=title,width=width,height=height,layout="grid",bg="white")
      #self.app = App()
      #self.app.display()
      #self.window = Window(app,title=title,width=width,height=height,layout="grid",bg="white")
'''
class NewWindow():
   
   def __init__(self,width, height, title):
      if not self.app:
         self.app = App(title=title,width=width,height=height,layout="grid",bg="white")
      self.window = Window(self.app,title=title,width=width,height=height,layout="grid",bg="white")
      self.window.show()
      
   def openFile(self,filename):
      self.contents = []
      with open(filename+".txt","r") as self.file:
         for line in self.file:
            self.contents.append(line.split(","))
      return self.contents

class Select(NewWindow,Database): #need to import from database to return database
  
  def __init__(self,height, width, title):
    super().__init__(height, width, title)
    
  #result = Database.returnSQL("SELECT className FROM classesTable") 
  #need to return the list of names
  #result = super().openFile()
   
    result = super().openFile("users")
    print(result)
    for entry in range(len(result)):
       self.button=PushButton(self.app ,text=result[entry][0],command=lambda:self.openUser(result[entry][1]),grid=[0,entry])
       #self.button.grid(row=entry)
    self.button = PushButton(self.app,text="New User...",command=self.newUser,grid=[0,len(result)])

  def test(self):
     print("test")

  def newUser(self):
     print("new user")
     self.window.hide()
     super().__init__(250, 100, "New User")
     self.text=Text(self.app,text="Enter the your name\nE.g. Mr Hirst",grid=[0,0])
     self.entry = TextBox(self.app,width=10)
     
     self.button = PushButton(self.app,text="Submit",command=self.submitNewUser,grid=[0,1])

  def submitNewUser(self):
     self.user = self.entry.get()
     self.user = self.user.replace(" ","")
     self.openUser(self.user)
     print("new database created")
     
