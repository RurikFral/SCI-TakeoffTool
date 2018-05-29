from tkinter import *
from tkinter import ttk
from Widgets.header import Header
from Widgets.street_calculator import StreetCalculator
from Services.router import RouterService

#main
root = Tk()
root.title("SCI - Steel Takeoff Tool")
root.resizable(width = False, height = False)

#build header
headerWidget = Header(root)

#initialize
root.config(menu = headerWidget.get())
root.mainloop()