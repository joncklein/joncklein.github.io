#####################################
##  Jonathan Klein
##  10339970
####################################
from Tkinter import *
from cars import *

'''problems:
    1. program occasionally crashes when taking more cars than in stock. Code deals with the issus but the interface can't handle it.
    2. unchecking a button has the same impact as checking it. 
    3. rent and return buttons can both be selected. Radiobutton would solve this, but this proved unworkable later in the code.'''

class Application(Frame):
    #initialise frame
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.electric_cars = []
        self.petrol_cars = []
        self.diesel_cars = []
        self.hybrid_cars = []
        self.create_current_stock()
        
    def create_widgets(self):
        #create label
        self.title = Label(self, text = "Select car type:    ")
        self.title.grid(row = 4, column = 1, columnspan = 2, sticky = W)
        #instruction text
        self.instruction1 = Label(self, text = "Would you like to rent or return:   ")
        self.instruction1.grid(row = 0, column = 1, columnspan = 2, sticky = W)
        
        #fields to enter numbers
        self.field1 = Entry(self)
        self.field1.grid(row = 3, column = 1, sticky = W)
        
        self.instruction2 = Label(self, text = "Enter number of cars:   ")
        self.instruction2.grid(row = 2, column = 1, columnspan = 2, sticky = W)
        
        #radiobutton would be a better choice here, but causes problems later on
        self.rent_button = BooleanVar()
        Checkbutton(self, text ="rent", variable = self.rent_button).grid(row = 1, column = 1, columnspan = 1, sticky = W)
		
        self.return_button = BooleanVar()
        Checkbutton(self, text ="return", variable = self.return_button).grid(row = 1, column = 2, columnspan = 1, sticky = W)
        
        #checkbuttons for functions
        self.petrol_button = BooleanVar() 
        Checkbutton(self, text ="petrol", variable = self.petrol_button, command = self.update_text).grid(row = 5, column = 1, sticky = W)
        
        self.diesel_button = BooleanVar() 
        Checkbutton(self, text ="diesel", variable = self.diesel_button, command = self.update_text).grid(row = 5, column = 2, sticky = W)
        
        self.electric_button = BooleanVar() 
        Checkbutton(self, text ="electric", variable = self.electric_button, command = self.update_text).grid(row = 6, column = 1, sticky = W)
        
        self.hybrid_button = BooleanVar() 
        Checkbutton(self, text ="hybrid", variable = self.hybrid_button, command = self.update_text).grid(row = 6, column = 2, sticky = W)
  
        self.text = Text(self, width = 20, height = 8, wrap = WORD)
        self.text.grid(row = 11, column = 1, sticky = W)
   
    
    def create_current_stock(self):
        for i in range(4):
           self.electric_cars.append(ElectricCar())
        for i in range(8):
           self.diesel_cars.append(DieselCar())
        for i in range(24):
           self.petrol_cars.append(PetrolCar())
        for i in range(4):
           self.hybrid_cars.append(HybridCar())
        
    
    def update_text(self):
        #result to be fed back out to user
        result = ""
        #deal with bad user input
        try:
            numbercars = int(self.field1.get())
        except:
            result += 'please enter number'
        
        #deal with rent and return options. Attempted to fit into function, but got some unusual bugs
        if self.petrol_button.get():
            #for rent button on
            if self.rent_button.get():
                total = 0
                while total < numbercars:
                    #this try except code tends to cause the program to crash
                    try:
                        self.petrol_cars.pop()
                        total = total + 1
                    except:
                        result += 'no petrol cars to rent'
                if len(self.petrol_cars) > 1:
                    result += 'petrol cars in stock: ' + str(len(self.petrol_cars)+numbercars)+'\n' 
                    #adds numbercars back to the output, allowing user to see cars in stock before the current amount is removed.
                elif len(self.petrol_cars) < 1:
                    result += 'no petrol cars to rent'
            #for return button
            elif self.return_button.get():
                for i in range(numbercars):
                    self.petrol_cars.append(PetrolCar())
                if len(self.petrol_cars) < 4:
                    result += 'petrol cars in stock: ' + str(len(self.petrol_cars))+'\n'   
                elif len(self.petrol_cars) > 4:
                    result += 'all cars in stock'
             
        #same as above    
        if self.diesel_button.get():
            if self.rent_button.get():
                total = 0
                while total < numbercars:
                    try:
                        self.diesel_cars.pop()
                        total = total + 1
                    except:
                        result += 'no diesel cars to rent'
                if len(self.diesel_cars) > 1:
                    result += 'diesel cars in stock: ' + str(len(self.diesel_cars))+'\n' 
                elif len(self.diesel_cars) < 1:
                    result += 'no diesel cars to rent'
            elif self.return_button.get():
                for i in range(numbercars):
                    self.diesel_cars.append(DieselCar())
                if len(self.diesel_cars) < 4:
                    result += 'diesel cars in stock: ' + str(len(self.diesel_cars))+'\n'   
                elif len(self.diesel_cars) > 4:
                    result += 'all cars in stock'
            
        
        if self.electric_button.get():
            if self.rent_button.get():
                total = 0
                while total < numbercars:
                    try:
                        self.electric_cars.pop()
                        total = total + 1
                    except:
                        result += 'no electric cars to rent'
                if len(self.electric_cars) > 1:
                    result += 'electric cars in stock: ' + str(len(self.electric_cars))+'\n' 
                elif len(self.electric_cars) < 1:
                    result += 'no electric cars to rent'
            elif self.return_button.get():
                for i in range(numbercars):
                    self.electric_cars.append(ElectricCar())
                if len(self.electric_cars) < 4:
                    result += 'electric cars in stock: ' + str(len(self.electric_cars))+'\n'   
                elif len(self.electric_cars) > 4:
                    result += 'all cars in stock'
            
        
        if self.hybrid_button.get():
            if self.rent_button.get():
                total = 0
                while total < numbercars:
                    try:
                        self.hybrid_cars.pop()
                        total = total + 1
                    except:
                        result += 'no hybrid cars to rent'
                if len(self.hybrid_cars) > 1:
                    result += 'hybrid cars in stock: ' + str(len(self.hybrid_cars))+'\n' 
                elif len(self.hybrid_cars) < 1:
                    result += 'no hybrid cars to rent'
            elif self.return_button.get():
                for i in range(numbercars):
                    self.hybrid_cars.append(HybridCar())
                if len(self.hybrid_cars) < 4:
                    result += 'hybrid cars in stock: ' + str(len(self.hybrid_cars))+'\n'   
                elif len(self.hybrid_cars) > 4:
                    result += 'all cars in stock' 
                    
        self.text.delete(0.0, END)    
        self.text.insert(0.0, result)
    

#set up GUI
root = Tk()
root.title("DBS Car Rental")
#set dimensions
root.geometry("320x300")

app = Application(root)

root.mainloop()