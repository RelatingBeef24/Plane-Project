class Engine(object):
    def __init__(self, x, y, size, win):
        self.x = x
        self.y = y
        self.size = size
        self.buildEngine(x, y, size, win)