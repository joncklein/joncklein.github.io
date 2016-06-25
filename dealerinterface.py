#####################################
##  Jonathan Klein
##  10339970
####################################
from Tkinter import *


class Application(Frame):
    #initialise frame
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        #create buttons
        self.title = Label(self, text = "Rent a car:    ")
        self.title.grid(row = 3, column = 1, columnspan = 2, sticky = W)
        #instruction text
        self.instruction1 = Label(self, text = "Would you like to rent a car:   ")
        self.instruction1.grid(row = 0, column = 1, columnspan = 2, sticky = W)
        
        self.instruction2 = Label(self, text = "Enter second number: ")
        self.instruction2.grid(row = 2, column = 1, columnspan = 2, sticky = W)
        #fields to enter numbers
        self.yes_button = Button(self, text ="yes") #command = self.petrol#)
        self.yes_button.grid(row = 1, column = 1, columnspan = 1, sticky = W)
		
        self.no_button = Button(self, text ="no") #command = self.petrol#)
        self.no_button.grid(row = 1, column = 2, sticky = W)
        
        # self.text = Text(self, width = 35, height = 5, wrap = WORD)
        # self.text.grid(row = 13, column = 1, sticky = W)
        #buttons for functions
        self.petrol_button = Button(self, text ="petrol",) #command = self.petrol#)
        self.petrol_button.grid(row = 4, column = 1, sticky = W)
        
        self.diesel_button = Button(self, text ="diesel",) #command = self.diesel#)
        self.diesel_button.grid(row = 4, column = 2)
        
        self.electric_button = Button(self, text ="electric",) #command = self.electric#)
        self.electric_button.grid(row = 6, column = 1, sticky = NW)
        
        self.hybrid_button = Button(self, text ="hybrid",) #command = self.hybrid#)
        self.hybrid_button.grid(row = 7, column = 1, sticky = NW)
  
    

#set up GUI
root = Tk()
root.title("DBS Car Rental")
#set dimensions
root.geometry("300x280")

app = Application(root)

root.mainloop()