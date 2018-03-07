from Graphics import *
class Engine(object):
    def __init__(self, x, radius, size, win):
        self.x = x
        self.radius = radius
        self.size = size
        self.buildEngine(x, radius, size, win)

    def buildEngine(self, x, radius, size, win):
        innerShell = Circle(Point(500,325))