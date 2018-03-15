from graphics import *
from Fuselage import *
from Wings import *
from Engine import *
from Prop import *






class Plane(object):
    def __init__(self,win):
        fuselage = Fuselage(color_rgb(199,204,203),win)
        wing = Wings("grey",win)
        # engine = Engine(0,win) #Don't worry about this, this is to test engine by itself
        prop = Prop(win)


def main():
    window = GraphWin("Plane", 1000, 650)
    tc = Plane(window)
    window.setBackground(color_rgb(123,224,221))
    window.getMouse()
    window.close()

main()
