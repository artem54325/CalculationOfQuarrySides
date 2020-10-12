import math

# from sympy import Symbol
import sympy as sym


class CalculationPoint:

    def equation12(self, y1, x1, x, y, p, q, f):

        answer1 = ((f - 2 * p) * math.sqrt(1 - q * q) + 2 * math.sqrt( f * f * q * q * ( 1 - q * 2 ) + p * ( p - f ))/
                   ( 2 * f * q * q + ( 2 * p - f) * q - f)) - (x - x1)/(y - y1)

        answer2 = ((f - 2 * p) * math.sqrt(1 - q * q) - 2 * math.sqrt( f * f * q * q * ( 1 - q * 2 ) + p * ( p - f ))/
                   ( 2 * f * q * q + ( 2 * p - f) * q - f)) - (x - x1)/(y - y1)

        return [answer1, answer2]


    def equation14(self, y1, x1, x, y, q1, p1, p, q, f,u):
        answer1 = (
                (2 * p - f * (1+2*q))*(q-q1)/(f-p) +
                (((y-y1)/(x-x1))*(2*p*q - f*q + 2*f*q*q-f)/ (math.sqrt(1-q*q)*f-p))*(q-q1) +
                u*(y-y1)*(2*p + f*(q-1))/(p*(f-p)) +
                u*(x-x1) * (f*(q*q -1))/(math.sqrt(1-q*q)*p*(f-p)) -
                4 * 1 / f * (p - p1)
                )
        return [answer1]

    def check (self, x,y):
        return x-y-3


if __name__ == "__main__":
    # u - объемный вес
    # f - коэффициент внутреннего трения
    u = 1
    f = math.tan(math.radians(30))
    # print(f, u)
    calc = CalculationPoint()
    # answ = calc.check(Symbol("y1"), Symbol("x1"))
    x = sym.Symbol('x')
    y = sym.Symbol('y')
    # answ = sym.solve((x-y-y), (x,y))
    # q = sym.nsolve(calc.check(x,y).subs('x',1), y,-5)
    # print(q)
    q = sym.nsolve(calc.equation12(x,y, 0, 0, 1.732, 1, f)[0].subs('x', 4), y, -5)

    print(q)
    # calc =  CalculationPoint(f, u)