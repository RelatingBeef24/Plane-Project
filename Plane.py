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

class Wings(object):
    def __init__(self,win):
        self.buildWings(win)

    def buildWings(self,win):
        wingP1 = Rectangle(Point(400, 325), Point(50, 350))
        wingTip = Arc(Point(75,325),Point(25,350), 90, 170)
        wingP2 = Polygon(Point(40,350),Point(400,400),Point(400,330),Point(40,330))
        wingTip.draw(win)
        wingTip.setOutline("grey")
        wingTip.setFill("grey")
        wingP1.draw(win)
        wingP1.setOutline("grey")
        wingP1.setFill("grey")
        wingP2.draw(win)
        wingP2.setOutline("grey")
        wingP2.setFill("grey")
        wing2p1 = Rectangle(Point(964, 325), Point(600, 350))
        wingTip2 = Arc(Point(975, 325), Point(950, 350), 90, -170)
        wing2P2 = Polygon(Point(960, 350), Point(600, 400), Point(600, 330), Point(960, 330))
        wingTip2.draw(win)
        wing2p1.draw(win)
        wing2P2.draw(win)
        wingTip2.setFill("grey")
        wingTip2.setOutline("grey")
        wing2p1.setFill("grey")
        wing2p1.setOutline("grey")
        wing2P2.setFill("grey")
        wing2P2.setOutline("grey")


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


class Prop(Engine):
    def __init__(self,win,size = 0):
        super(Prop, self).__init__(size,win)
        self.buildProp(win)
    def buildProp(self,win):

        blade = Rectangle(Point(270 - self.size,351-self.size),Point(280+self.size,270 - self.size * 5))
        blade.draw(win)
        blade2 = Rectangle(Point(270 - self.size,442+self.size* 5),Point(280 + self.size,361 + self.size))
        blade2.draw(win)
        blade.setFill("grey")
        blade2.setFill("grey")

        blade2ndEng = Rectangle(Point(720 - self.size,351-self.size),Point(730+self.size,270 - self.size * 5))
        blade2ndEng.draw(win)
        blade2ndEng2 = Rectangle(Point(720- self.size,442+self.size * 5),Point(730 + self.size,361 + self.size))
        blade2ndEng2.draw(win)
        blade2ndEng.setFill("grey")
        blade2ndEng2.setFill("grey")
class Plane(object):
    def __init__(self,win):
        fuselage = Fuselage(color_rgb(199,204,203),win)
        wing = Wings(win)
        # engine = Engine(0,win) #Don't worry about this for now
        prop = Prop(win,0)


def main():
    window = GraphWin("Plane", 1000, 650)
    tc = Plane(window)
    window.setBackground(color_rgb(123,224,221))
    window.getMouse()
    window.close()

main()
