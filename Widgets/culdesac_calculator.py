from tkinter import *
from tkinter import ttk
from Services.helpers import HelperService

class CuldesacCalculator:
    def __init__ (self, root):
        #variables
        self.radius = StringVar()
        self.centerToCenter = StringVar()
        self.overlap = StringVar()
        self.totalNumberOfBars = StringVar()

        #services
        self.helperService = HelperService()
        
        #display
        self.frame = Frame(root)

        #row0
        Label(self.frame, text = "Radius").grid(row = 0, column = 0, sticky = E, padx = (5,5), pady = (5,5))

        self.radiusEntry = Entry(self.frame,textvariable = self.radius, width = 20)
        self.radiusEntry.grid(row = 0, column = 1)

        Label(self.frame, text = "ft.").grid(row = 0, column = 2, sticky = W, padx = (5,5), pady = (5,5))

        #row1
        Label(self.frame, text = "Center to Center").grid(row = 1, column = 0, sticky = E, padx = (5,5), pady = (5,5))

        self.centerToCenterEntry = Entry(self.frame, textvariable = self.centerToCenter, width = 20)
        self.centerToCenterEntry.grid(row = 1, column = 1)

        Label(self.frame, text = "in.").grid(row = 1, column = 2, sticky = W, padx = (5,5), pady = (5,5))

        #row3
        Label(self.frame, text = "Logitudinal Overlap").grid(row = 3, column = 0, sticky = E, padx = (5,5), pady = (5,5))

        self.overlapEntry = Entry(self.frame, textvariable = self.overlap, width = 20)
        self.overlapEntry.grid(row = 3, column = 1)

        Label(self.frame, text = "in.").grid(row = 3, column = 2, sticky = W, padx = (5,5), pady = (5,5))

        #row5
        ttk.Separator(self.frame).grid(row = 5, columnspan = 5, sticky = E+W)

        #row6
        Label(self.frame, text = "Total 40' Uncut Bars:").grid(row = 6, column = 0, sticky = E, padx = (5,5), pady = (5,5))

        Label(self.frame, textvariable = self.totalNumberOfBars).grid(row = 6, column = 1, sticky = W, padx = (5,5), pady = (5,5))

        #calc buttons
        self.calcButton = Button(self.frame, text = "Calculate", command = self.calculateTotal)
        self.calcButton.grid(row = 1, column = 3, columnspan = 2, padx = (5,5), pady = (5,5), sticky=N+S+E+W)

        self.clearButton = Button(self.frame, text = "Clear", command = self.clearValues)
        self.clearButton.grid(row = 0, column = 3, columnspan = 2, padx = (5,5), pady = (5,5), sticky=N+S+E+W)


    def calculateTotal(self, event=None): 
        #get values from entry 
        radiusFloat = self.helperService.safe_cast(self.radius.get(), float, 0)
        centerToCenterFloat = self.helperService.safe_cast(self.centerToCenter.get(), float, 0)/12 #inches to feet
        defaultBarLength = 40
        overlapFloat = self.helperService.safe_cast(self.overlap.get(), float, 0)/12 #inches to feet

        #calculate totals based on inputs
        try:
            self.totalNumberOfBars.set(str(int(round((8*radiusFloat*radiusFloat)/(centerToCenterFloat*(defaultBarLength-overlapFloat))))))        
        except Exception as e:
            print(e)
            self.totalNumberOfBars.set("ERROR CALCULATING")
                    
        return 

    def clearValues(self, event=None):
        self.radius.set("")
        self.centerToCenter.set("")
        self.overlap.set("")
        self.totalNumberOfBars.set("")
        return

    def destory(self):
        self.frame.destroy()
        return
    
    def get(self):
        return self.frame