import math
from sympy import Symbol, integrate, nsolve



class CalculationPlasticityCriterion:
    def __init__(self, C, k, phi):
        self.sigm1 = Symbol('sigm1')
        self.sigm3 = Symbol('sigm3')
        tangPhi = math.tan(phi)
        self.func # переменная внутри которой будут происходит вычесления
        if(k == 0):
            self.func = self.sigm1 - self.sigm3 - 2 * C * \
                        math.sqrt((1 + tangPhi * self.sigm1 / C) * (1 + tangPhi * k * self.sigm3 / C))
        elif(k > 0 & k <= 1):
            self.func = self.sigm1 - self.sigm3 - 2 * C * tangPhi
        else:
            raise ArithmeticError('k выходит за горизонт')


    def getSigm1(self):
        pass
    def getSigm3(self):
        pass
