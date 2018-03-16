from graphics import *

class Fuselage(object):
    """Creates the body of the plane."""
    def __init__(self, color,win):
        self.color = color
        self.buildFuselage(win)
        self.buildWindscreen(win)
        self.buildTail(win)
    def buildFuselage(self, win):
        base = Polygon(Point(500, 250), Point(550, 260), Point(580, 270), Point(590, 275), Point(600, 290),
                       Point(600, 390), Point(600, 400), Point(575, 430), Point(550, 450), Point(450, 450),
                       Point(425, 430), Point(400, 400), Point(400, 390), Point(400, 290), Point(415, 275),
                       Point(450, 260))
        base.setFill(self.color)
        base.draw(win)
        arc = Arc(Point(400, 375), Point(600, 450), 15, 150)
        arc.draw(win)
        arc.setFill(color_rgb(172, 175, 175))
    def buildWindscreen(self,win):
        left = Polygon(Point(400,325),Point(420,290),Point(495,290),Point(495,325))
        left.setFill("blue")
        left.draw(win)
        right = Polygon(Point(505,290),Point(505,325),Point(600,325),Point(580,290))
        right.setFill("blue")
        right.draw(win)

    def buildTail(self,win):
        base = Polygon(Point(500,100),Point(495,250),Point(505,250))
        base.setFill(self.color)
        base.draw(win)
