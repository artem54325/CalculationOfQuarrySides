import cmath
import math


class Point:
    # def __init__(self, x, y, p, q):
    #     self.x = x
    #     self.y = y
    #     self.p = p
    #     self.q = q

    def __init__(self, x, y, p, q, alpha=None, betta=None):
        self.x = x
        self.y = y
        self.p = p
        self.q = q
        self.alpha = alpha
        self.betta = betta

    def getX(self):
        return (self.x)

    def getY(self):
        return (self.y)

    def getP(self):
        return (self.p)

    def getQ(self):
        return (self.q)

    def getAlpha(self, f):
        # if(self.alpha != None):
        #     return self.alpha
        return (self.getP() * self.getP() - 1) / f

    def getBetta(self, f):
        # if (self.betta != None):
        #     return self.betta
        return self.getAlpha(f) - 2 * self.getP()

    def setTable(self, x, y):
        self.tableX = x
        self.tableY = y

    def __repr__(self):# 0.5777
        try:
            return "<x:%s y:%s p:%s q:%s a1:%s b1:%s>" % (round(float(self.x),3), round(float(self.y),3), round(float(self.p),3),
                                                      round(float(self.q),3), round(float(self.getAlpha(0.577)),3),round(float(self.getBetta(0.577)),3))
        except Exception:
            print("Error")


