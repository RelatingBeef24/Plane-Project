from graphics import *
class Fuselage(object):
    def __init__(self, color,win):
        self.color = color
        self.buildFuselage(win)

    def buildFuselage(self, win):
        base = Polygon(Point(500,250), Point(550,260),Point(580,270),Point(590,275),Point(600,290),Point(600,390),Point(600,400), Point(575,430), Point(550,450),Point(450,450),Point(425,430),Point(400,400),Point(400,390),Point(400,290),Point(415,275),Point(450,260))
        base.setFill(self.color)
        base.draw(win)
        arc = Arc(Point(400, 375), Point(600, 450), 15, 150)
        arc.draw(win)
        arc.setFill(color_rgb(172,175,175))

