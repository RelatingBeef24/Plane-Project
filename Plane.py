from graphics import *


class Fuselage(object):
    def __init__(self, color):
        self.color = color

    def buildFuselage(self, win):
        base = Polygon(Point(500,250), Point(550,260),Point(580,270),Point(590,275),Point(600,290),Point(600,390),Point(600,400), Point(575,430), Point(550,450),Point(450,450),Point(425,430),Point(400,400),Point(400,390),Point(400,290),Point(415,275),Point(450,260))
        base.setFill(self.color)
        base.draw(win)
        arc = Arc(Point(400, 375), Point(600, 450), 15, 150)
        arc.draw(win)
        arc.setFill("grey")

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
        wing2p1 = Rectangle(Point(964, 325), Point(600, 350))
        wingTip2 = Arc(Point(975, 325), Point(950, 350), 90, -170)
        wing2P2 = Polygon(Point(960, 350), Point(600, 400), Point(600, 330), Point(960, 330))
        wingTip2.draw(win)
        wing2p1.draw(win)
        wing2P2.draw(win)
        wingTip2.setFill(self.color)
        wingTip2.setOutline(self.color)
        wing2p1.setFill(self.color)
        wing2p1.setOutline(self.color)
        wing2P2.setFill(self.color)
        wing2P2.setOutline(self.color)

class Engine(object):
    def __init__(self, size = 0):
        self.size = size

    def buildBase(self,win):
        base = RoundedRectangle(Point(225 - (self.size*10),312 - (self.size*10)),Point(325 + (self.size*10),400 + (self.size*10)))
        base.draw(win)
        base2 = RoundedRectangle(Point(675 - (self.size*10),312 - (self.size*10)), Point(775 + (self.size*10), 400 + (self.size*10)))
        base2.draw(win)

    def buildHub(self,win):
        cap = Circle(Point(275,356), 5 + self.size)
        cap.draw(win)
        cap2 = Circle(Point(725,356), 5 + self.size)
        cap2.draw(win)

class Prop(Engine):
    def __init__(self, props):
        super(Prop, self).__init__(props)
        self.props = props
    def prop(self, props):
        blade = Rectangle
class Plane(object):
    def __init__(self,win):
        fuselage = Fuselage("green")
        fuselage.buildFuselage(win)
        wing = Wings("red")
        wing.buildWings(win)
        engine = Engine(0)
        engine.buildBase(win)
        engine.buildHub(win)

def main():
    window = GraphWin("Plane", 1000, 650)
    tc = Plane(window)
    window.getMouse()
    window.close()

main()
