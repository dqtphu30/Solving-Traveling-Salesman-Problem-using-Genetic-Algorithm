import math

class City:
    def __init__(self, symbol, x=None, y=None):
        self.symbol = symbol
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getSymbol(self):
        return self.symbol

    def get_coordinates(self):
        return [self.x, self.y]
    
    def distanceTo(self, city):
        xDistance = abs(self.getX() - city.getX())
        yDistance = abs(self.getY() - city.getY())
        distance = math.sqrt((xDistance * xDistance) + (yDistance * yDistance))
        return distance

    def __repr__(self):
        return self.getSymbol() + ', ' + str(self.getX()) + ", " + str(self.getY())