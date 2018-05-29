from tkinter import *
from tkinter import ttk
from Services.router import RouterService

class Header:
    def __init__ (self, root):
        self.root = root
        self.router = RouterService(root)

        #main menu setup
        self.mainMenu = Menu(root)
        #file menu
        fileMenu = Menu(self.mainMenu, tearoff = 0)
        fileMenu.add_command(label = "Quit", command = self.__quitApp)
        #calculators menu
        calcMenu = Menu(self.mainMenu, tearoff = 0)
        calcMenu.add_command(label = "Street", command = self.__goStreetCalc)
        calcMenu.add_command(label = "Cul-de-sac", command = self.__goCuldesacCalc)
        calcMenu.add_command(label = "Eyebrow", command = self.__goEyebrowCalc)
        #help menu
        helpMenu = Menu(self.mainMenu, tearoff = 0)
        helpMenu.add_command(label = "About", command = self.__goAboutCalc)
        #add cascades
        self.mainMenu.add_cascade(label = "File", menu = fileMenu)
        self.mainMenu.add_cascade(label = "Calculators", menu = calcMenu)
        self.mainMenu.add_cascade(label = "Help", menu = helpMenu)

    def get(self):
        return self.mainMenu

    def __goStreetCalc(self):
        self.router.go("StreetCalculator")
    
    def __goCuldesacCalc(self):
        self.router.go("CuldesacCalculator")
    
    def __goEyebrowCalc(self):
        self.router.go("EyebrowCalculator")
    
    def __goAboutCalc(self):
        self.router.go("About")

    def __quitApp(self):
        self.root.quit()