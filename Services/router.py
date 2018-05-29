from Widgets.street_calculator import StreetCalculator
from Widgets.eyebrow_calculator import EyebrowCalculator
from Widgets.culdesac_calculator import CuldesacCalculator

class RouterState:
    _sharedState = {}
    def __init__(self):
        self.__dict__ = self._sharedState

class RouterService(RouterState):
    def __init__ (self, root):
        #get shared state for this instance
        RouterState.__init__(self)
        #initialize states
        self.root = root
        self.currentState = None
        self.states = []
        self.states.append(State("StreetCalculator", "StreetCalculator"))
        self.states.append(State("EyebrowCalculator", "EyebrowCalculator"))
        self.states.append(State("CuldesacCalculator", "CuldesacCalculator"))

        #if there is no current state (initialized for the first time or on some other time with no shared state). set the default state
        if self.currentState == None:
            self.go("StreetCalculator")
            
    def go(self, name, data = None):
        for state in self.states:
            if state.name == name:
                if self.currentState != None:
                    #destroy existing current frame
                    self.currentState.get().destroy()
                #set and pack the new frame
                self.currentState = eval(state.className)(self.root)
                self.currentState.get().pack()
                break
        
class State:
    def __init__ (self, name, className):
        self.name = name
        self.className = className
