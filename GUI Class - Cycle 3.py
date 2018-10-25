from tkinter import *
from DatabaseClassv2 import Database
class GUI:

   def __init__(self,width, height, title, root):
    #set clour
    #set dimensions
    #set resizable
    #self.root = Tk()
    self.root = root
    root.title(title)
    #self.frame = Frame(self.root)
    #self.root.title("{}").format(title)
    dimension = str(width)+"x"+str(height)
    self.root.geometry(dimension)
    #self.root.geometry("{}x{}").format(height,width)
    self.root.resizable (False, False)
    self.root.configure(background = "white")

    #self.root.mainloop() we need this not sure where!
   def runWindow(self):
    self.root.mainloop()

   def openFile(self,filename):
    self.contents = []
    with open(filename+".txt","r") as self.file:
       for line in self.file:
          self.contents.append(line.split(","))
       return self.contents


class Select(GUI,Database): #need to import from database to return database
  
  def __init__(self,height, width, title, root):
    super().__init__(height, width, title, root)
    
  #result = Database.returnSQL("SELECT className FROM classesTable") 
  #need to return the list of names
  #result = super().openFile()
   
    result = super().openFile("users")
    print(result)
    for entry in range(len(result)):
       self.button=Button(self.root,text=result[entry][0],command=lambda:self.openUser(result[entry][1]))
       self.button.grid(row=entry)
    self.button = Button(self.root,text="New User...",command=self.newUser).grid(row=len(result)

  def newUser(self):
     print("new user")
     self.root.destroy()
     super().__init__(250, 100, "New User", Tk())
     self.label=Label(self.root,text="Enter the your name\nE.g. Mr Hirst").grid(row=0)
     self.entry = Entry(self.root,width=10)
     self.entry.grid(row=1)
     self.button = Button(self.root,text="Submit",command=self.submitNewUser).grid(row=2)

  def submitNewUser(self):
     self.user = self.entry.get()
     self.user = self.user.replace(" ","")
     self.openUser(self.user)
     print("new database created")
