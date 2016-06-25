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
        self.title = Label(self, text = "Select car type:    ")
        self.title.grid(row = 3, column = 1, columnspan = 2, sticky = W)
        #instruction text
        self.instruction1 = Label(self, text = "Would you like to rent or return:   ")
        self.instruction1.grid(row = 0, column = 1, columnspan = 2, sticky = W)
        
        #fields to enter numbers
        self.rent_button = Radiobutton(self, text ="rent", value = 1) #command = self.petrol#)
        self.rent_button.grid(row = 1, column = 1, columnspan = 1, sticky = W)
		
        self.return_button = Radiobutton(self, text ="return", value = 2) #command = self.petrol#)
        self.return_button.grid(row = 1, column = 2, sticky = W)
        
        #buttons for functions
        self.petrol_button = Checkbutton(self, text ="petrol",) #command = self.petrol#)
        self.petrol_button.grid(row = 4, column = 1, sticky = W)
        
        self.diesel_button = Checkbutton(self, text ="diesel",) #command = self.diesel#)
        self.diesel_button.grid(row = 4, column = 2)
        
        self.electric_button = Checkbutton(self, text ="electric",) #command = self.electric#)
        self.electric_button.grid(row = 6, column = 1, sticky = NW)
        
        self.hybrid_button = Checkbutton(self, text ="hybrid",) #command = self.hybrid#)
        self.hybrid_button.grid(row = 6, column = 2, sticky = W)
  
        self.text = Text(self, width = 20, height = 5, wrap = WORD)
        self.text.grid(row = 7, column = 1, sticky = W)
    

#set up GUI
root = Tk()
root.title("DBS Car Rental")
#set dimensions
root.geometry("300x280")

app = Application(root)

root.mainloop()