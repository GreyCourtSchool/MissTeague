from tkinter import *
Class GUI:

  def __init__(self,height, width, title):
    #set clour
    #set dimensions
    #set resizable
    self.root = Tk()
    self.root.title("{}").format(title)
    self.root.geometry("{}x{}").format(height,width)
    self.root.resizable (False, False)
    self.root.configure(background = "white")

Class Select(GUI,Database): #need to import from database to return database
  
  def __init__(self,height, width, title):
    super().__init__(self,height, width, title)
    
    
  #need to return the list of names  
  for i,url in enumerate(url_list):
    label=tk.Label(frame,text=url)
    label.grid(row=i)
    label.bind("<Button-1>",lambda e,url=url:open_url(url))
  
    
    
