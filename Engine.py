from graphics import *

"""The important bit"""
class Engine(object):
    def __init__(self, size,win):
        self.size = size
        self.buildBase(win)
        self.buildCowling(win)
        self.buildHub(win)

    def buildBase(self,win):
        base = RoundedRectangle(Point(225 - (self.size*5),312 - (self.size*5)),Point(325 + (self.size*5),400 + (self.size*5)))
        base.draw(win)
        base2 = RoundedRectangle(Point(675 - (self.size*5),312 - (self.size*5)), Point(775 + (self.size*5), 400 + (self.size*5)))
        base2.draw(win)
        base.setFill(color_rgb(49,73,112))
        base2.setFill(color_rgb(49,73,112))

    def buildCowling(self,win):
        cap = Circle(Point(275,356), 25 + self.size)
        cap.draw(win)
        cap2 = Circle(Point(725,356), 25 + self.size)
        cap2.draw(win)
        cap.setFill("black")
        cap2.setFill("black")

    def buildHub(self,win):
        cap = Circle(Point(275,356), 5 + self.size)
        cap.draw(win)
        cap2 = Circle(Point(725,356), 5 + self.size)
        cap2.draw(win)
        cap.setFill("maroon")
        cap2.setFill("maroon")