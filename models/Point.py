class Point:
    def __init__(self, x, y, p, q):
        self.x = x
        self.y = y
        self.p = p
        self.q = q

    def getX(self):
        return float(self.x)

    def getY(self):
        return float(self.y)

    def getP(self):
        return float(self.p)

    def getQ(self):
        return float(self.q)

    def getAlpha(self, f):
        return (self.p**2-1)/f

    def getBetta(self, f):
        return self.getAlpha(f)-2*self.p

    def __repr__(self):
        return "<x:%s y:%s p:%s q:%s>" % (round(float(self.x),3), round(float(self.y),3), round(float(self.p),3), round(float(self.q),3))

