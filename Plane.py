from Fuselage import *
from Wings import *
from Prop import *

class Plane(object):
    """Brings all of the plane parts together."""
    def __init__(self,win):
        fuselage = Fuselage(color_rgb(199,204,203),win)
        wing = Wings("grey",win)
        #engine = Engine(0,win) #Don't worry about this. Unhashtag this to test engine by itself
        prop = Prop(win,0) #Size is changable through here


def main():
    window = GraphWin("Plane", 1000, 650)
    tortshwar = Plane(window)
    window.setBackground(color_rgb(123,224,221))
    window.getMouse()
    window.close()

main()
