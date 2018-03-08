from graphics import *


class Fuselage(object):
    def __init__(self, color):
        self.color = color

    def buildFuselage(self, win):
        base = Polygon(Point(500,250), Point(550,260),Point(580,270),Point(590,275),Point(600,290),Point(600,390),Point(590,400), Point(575,430), Point(550,450),Point(450,450),Point(425,430),Point(415,400),Point(400,390),Point(400,290),Point(415,275),Point(450,260))
        base.setFill(self.color)
        base.draw(win)

class Wings(Object):
    def __init__(self):


class Plane(object):
    def __init__(self,win):
        fuselage = Fuselage("green")
        fuselage.buildFuselage(win)

def main():
    window = GraphWin("Plane", 1000, 650)
    tc = Plane(window)
    window.getMouse()
    window.close()

main()
