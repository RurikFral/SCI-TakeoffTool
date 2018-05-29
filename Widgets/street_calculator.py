from tkinter import *
from tkinter import ttk
from Services.helpers import HelperService
import math

class StreetCalculator:
    def __init__ (self, root):
        #variables
        self.width = StringVar()
        self.length = StringVar()
        self.centerToCenter = StringVar()
        self.overlap = StringVar()
        self.hasCurbSteel = IntVar()
        self.totalNumberOfBars = StringVar()
        self.totalNumberOfCutBars = StringVar()

        #services
        self.helperService = HelperService()
        
        #display
        self.frame = Frame(root)

        #row0
        Label(self.frame, text = "Width").grid(row = 0, column = 0, sticky = E, padx = (5,5), pady = (5,5))

        self.widthEntry = Entry(self.frame,textvariable = self.width, width = 20)
        self.widthEntry.grid(row = 0, column = 1)

        Label(self.frame, text = "ft.").grid(row = 0, column = 2, sticky = W, padx = (5,5), pady = (5,5))

        #row1
        Label(self.frame, text = "Length").grid(row = 1, column = 0, sticky = E, padx = (5,5), pady = (5,5))

        self.lengthEntry = Entry(self.frame, textvariable = self.length, width = 20)
        self.lengthEntry.grid(row = 1, column = 1)

        Label(self.frame, text = "ft.").grid(row = 1, column = 2, sticky = W, padx = (5,5), pady = (5,5))

        #row2
        Label(self.frame, text = "Center to Center").grid(row = 2, column = 0, sticky = E, padx = (5,5), pady = (5,5))

        self.centerToCenterEntry = Entry(self.frame, textvariable = self.centerToCenter, width = 20)
        self.centerToCenterEntry.grid(row = 2, column = 1)

        Label(self.frame, text = "in.").grid(row = 2, column = 2, sticky = W, padx = (5,5), pady = (5,5))

        #row3
        Label(self.frame, text = "Logitudinal Overlap").grid(row = 3, column = 0, sticky = E, padx = (5,5), pady = (5,5))

        self.overlapEntry = Entry(self.frame, textvariable = self.overlap, width = 20)
        self.overlapEntry.grid(row = 3, column = 1)

        Label(self.frame, text = "in.").grid(row = 3, column = 2, sticky = W, padx = (5,5), pady = (5,5))

        #row4
        Label(self.frame, text = "Has curb steel?").grid(row = 4, column = 0, sticky = E, padx = (5,5), pady = (5,5))

        Checkbutton(self.frame, variable = self.hasCurbSteel, onvalue = 2).grid(row = 4, column = 1, sticky = W, padx = (5,5), pady = (5,5))

        #row5
        ttk.Separator(self.frame).grid(row = 5, columnspan = 5, sticky = E+W)

        #row6
        Label(self.frame, text = "Total 40' Uncut Bars:").grid(row = 6, column = 0, sticky = E, padx = (5,5), pady = (5,5))

        Label(self.frame, textvariable = self.totalNumberOfBars).grid(row = 6, column = 1, sticky = W, padx = (5,5), pady = (5,5))

        #row7
        Label(self.frame, text = "Total Custom Cut Bars:").grid(row = 7, column = 0, sticky = E, padx = (5,5), pady = (5,5))

        Label(self.frame, textvariable = self.totalNumberOfCutBars).grid(row = 7, column = 1, sticky = W, padx = (5,5), pady = (5,5))

        #calc buttons
        self.calcButton = Button(self.frame, text = "Calculate", command = self.calculateTotal)
        self.calcButton.grid(row = 1, column = 3, columnspan = 2, padx = (5,5), pady = (5,5), sticky=N+S+E+W)

        self.clearButton = Button(self.frame, text = "Clear", command = self.clearValues)
        self.clearButton.grid(row = 0, column = 3, columnspan = 2, padx = (5,5), pady = (5,5), sticky=N+S+E+W)

    def calculateTotal(self, event=None):
        #get values from entry 
        runLengthFloat = self.helperService.safe_cast(self.length.get(), float, 0)
        widthFloat = self.helperService.safe_cast(self.width.get(), float, 0)
        centerToCenterFloat = self.helperService.safe_cast(self.centerToCenter.get(), float, 0)/12 #inches to feet
        defaultBarLength = 40
        defaultTransverseOffset = 0.5
        overlapFloat = self.helperService.safe_cast(self.overlap.get(), float, 0)/12 #inches to feet

        #calculate totals based on inputs
        try:
            self.totalNumberOfBars.set(str(int(round((runLengthFloat*(math.floor((widthFloat/centerToCenterFloat)+self.hasCurbSteel.get()+1)))/(defaultBarLength-overlapFloat)))))        
        except Exception as e:
            print(e)
            self.totalNumberOfBars.set("ERROR CALCULATING")

        try:
            self.totalNumberOfCutBars.set(str(int(round(runLengthFloat/centerToCenterFloat))) + " at " + str(widthFloat-defaultTransverseOffset) + " ft.")
        except Exception as e:
            print(e)
            self.totalNumberOfCutBars.set("ERROR CALCULATING")
                    
        return 

    def clearValues(self, event=None):
        self.length.set("")
        self.width.set("")
        self.centerToCenter.set("")
        self.overlap.set("")
        self.hasCurbSteel.set(0)
        self.totalNumberOfBars.set("")
        self.totalNumberOfCutBars.set("")

    def destory(self):
        self.frame.destroy()
    
    def get(self):
        return self.frame