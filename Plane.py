from graphics import *


class Fuselage(object):
    def __init__(self, color):
        self.color = color

    def buildFuselage(self, win):
        base = Polygon(Point(500,250), Point(550,260),Point(580,270),Point(590,275),Point(600,290),Point(600,390),Point(600,400), Point(575,430), Point(550,450),Point(450,450),Point(425,430),Point(400,400),Point(400,390),Point(400,290),Point(415,275),Point(450,260))
        base.setFill(self.color)
        base.draw(win)

class Wings(object):
    def __init__(self, color):
        self.color = color

    def buildWings(self,win):
        wingP1 = Rectangle(Point(400, 325), Point(50, 350))
        wingTip = Arc(Point(75,325),Point(25,350), 90, 170)
        wingP2 = Polygon(Point(40,350),Point(400,400),Point(400,330),Point(40,330))
        wingTip.draw(win)
        wingTip.setOutline(self.color)
        wingTip.setFill(self.color)
        wingP1.draw(win)
        wingP1.setOutline(self.color)
        wingP1.setFill(self.color)
        wingP2.draw(win)
        wingP2.setOutline(self.color)
        wingP2.setFill(self.color)
        wing2p1 = Rectangle(Point(950, 325), Point(600, 350))
        wingTip = Arc(Point(975, 325), Point(950, 350), 90, 170)
        wingTip.draw(win)
        wing2p1.draw(win)

# class Engine(object):
#     def __init__(self, size):
#         self.size = size
#
#     def buildEngine(self):
#         base = RoundedRectangle(Point(34))
class Plane(object):
    def __init__(self,win):
        fuselage = Fuselage("green")
        fuselage.buildFuselage(win)
        wing = Wings("red")
        wing.buildWings(win)
def main():
    window = GraphWin("Plane", 1000, 650)
    tc = Plane(window)
    window.getMouse()
    window.close()

main()
