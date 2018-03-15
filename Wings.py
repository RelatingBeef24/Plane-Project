from graphics import *

class Wings(object):
    """Allows the plane to fly."""
    def __init__(self,color,win):
        self.color = color
        self.buildWings(win)

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
