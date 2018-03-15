from Engine import *

class Prop(Engine):
    """Creates the prop for the engines. Uses the engine class"""
    def __init__(self,win,size = 0):
        super(Prop, self).__init__(size,win)
        self.buildProp(win)

    def buildProp(self,win):
        """Props for the left engine"""
        blade = Rectangle(Point(270 - self.size,351-self.size),Point(280+self.size,270 - self.size * 5))
        blade.draw(win)
        blade2 = Rectangle(Point(270 - self.size,442+self.size* 5),Point(280 + self.size,361 + self.size))
        blade2.draw(win)
        blade.setFill("grey")
        blade2.setFill("grey")
        """Props for the right engine"""
        blade2ndEng = Rectangle(Point(720 - self.size,351-self.size),Point(730+self.size,270 - self.size * 5))
        blade2ndEng.draw(win)
        blade2ndEng2 = Rectangle(Point(720- self.size,442+self.size * 5),Point(730 + self.size,361 + self.size))
        blade2ndEng2.draw(win)
        blade2ndEng.setFill("grey")
        blade2ndEng2.setFill("grey")