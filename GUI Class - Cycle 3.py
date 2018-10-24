from tkinter import *
from DatabaseClass import Database
class GUI:

   def __init__(self,width, height, title):
    #set clour
    #set dimensions
    #set resizable
    self.root = Tk()
    self.root.title(title)
    #self.root.title("{}").format(title)
    dimension = str(width)+"x"+str(height)
    self.root.geometry(dimension)
    #self.root.geometry("{}x{}").format(height,width)
    self.root.resizable (False, False)
    self.root.configure(background = "white")

    #self.root.mainloop() we need this not sure where!
  def runWindow(self):
    self.root.mainloop()

  def openFile(filename):
    file = open(filename+".text",r)
    #needs to open the file
    #pull out the data
    #return list of contents

class Select(GUI): #need to import from database to return database
  
  def __init__(self,height, width, title):
    super().__init__(self,height, width, title)
    
  #result = Database.returnSQL("SELECT className FROM classesTable") 
  #need to return the list of names
  result = super().openFile()
  for i,result in enumerate(result):
    label=self.root.Label(frame,text=result)
    label.grid(row=i)
    #label.bind("<Button-1>",lambda e,url=url:open_url(url))


