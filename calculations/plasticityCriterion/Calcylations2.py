import math

import sympy as sym
import z3 as z3


class CalculationPoint2:

    def equation12(self, x, y, p, q, f, x1, y1):

        eq1 = (((f - 2 * p) * sym.sqrt(1 - q * q) +
                    2 * sym.sqrt( f * f * q * q * ( 1 - q * 2 ) + p * ( p - f ))) /
                   ( 2 * f * q * q + ( 2 * p - f) * q - f)) - ((y - y1) / (x - x1))

        eq2 = (((f - 2 * p) * sym.sqrt(1 - q * q) - # Здесь менять
                    2 * sym.sqrt( f * f * q * q * ( 1 - q * 2 ) + p * ( p - f ))) /
                   ( 2 * f * q * q + ( 2 * p - f) * q - f)) - ((y - y1) / (x - x1))


        return [eq1, eq2]

    # def equation12(self, x, y, p, q, f):
    #
    #     eq = (((f - 2 * p) * math.sqrt(1 - q * q) + # Здесь менять
    #                 2 * math.sqrt( f * f * q * q * ( 1 - q * 2 ) + p * ( p - f ))) /
    #                ( 2 * f * q * q + ( 2 * p - f) * q - f))
    #
    #     x1 = z3.BitVec('x1', 128)
    #     y1 = z3.BitVec('y1', 128)
    #
    #     solver = z3.Solver()
    #
    #     constraints = [
    #         x - (y - y1) / eq == x1,
    #         y - eq * (x-x1) == y1
    #     ]
    #     answer = []
    #     for i in constraints:
    #         solver.add(i)  # добавляем условия в солвер
    #     while solver.check() == z3.sat:
    #         print(solver.model()[x1], solver.model()[y1])  # если решение есть, выводим на экран x и y
    #         answer = solver.model()[x1], solver.model()[y1]
    #         solver.add(x1 != solver.model()[x1],
    #                    y1 != solver.model()[y1])
    #
    #     return answer


    def equation14(self, x, y, p, q, f, u, x1, y1, p1, q1):

        answer1 = (
                (2 * p - f * (1 + 2 * q))*(q - q1)/(f - p) +
                (((y-y1)/(x-x1))*(2 * p * q - f * q + 2 * f * q * q - f) / (sym.sqrt(1 + q * q) * f - p)) * ( q - q1) +
                u * (y - y1) * (2 * p + f * (q - 1))/(p * (f - p)) +
                u * (x - x1) * (f * (q * q - 1))/(sym.sqrt(1 + q * q) * p * (f - p)) -
                4 * 1 / f * (p - p1)    # left side
                )

        return answer1


if __name__ == "__main__":
    # u - объемный вес
    # f - коэффициент внутреннего трения
    calc = CalculationPoint2()
    u = 1
    f = math.tan(math.radians(30))
    p = sym.Symbol('p')#z3.BitVec('p', 128)
    q = sym.Symbol('q')#z3.BitVec('q', 128)
    p1 = 1.732 # sym.Symbol('p1')#z3.BitVec('p', 128)
    q1 = 1 # sym.Symbol('q1')#z3.BitVec('q', 128)
    x = sym.Symbol('x')
    y = sym.Symbol('y')
    x1 = 0
    y1 = 0
    #q = 1
    #p = 1.732
    # print(f, u)
    # answ = calc.check(Symbol("y1"), Symbol("x1"))
    # x = sym.Symbol('x')
    # y = sym.Symbol('y')
    # answ = sym.solve((x-y-y), (x,y))
    # q = sym.nsolve(calc.check(x,y).subs('x',1), y,-5)
    # print(q)
    p = 1
    q = 1.732
    # y = 1
    # print(calc.equation14(x, y, p, q, f, u, x1, y1, p1, q1))
    we = sym.nsolve(calc.equation14(x, y, p, q, f, u, x1, y1, p1, q1), (x), -1)
    # q = calc.equation12(0, 0, p, q, f)
    # p = 1
    # q = 1.742
    # x = 0
    # eqs = calc.equation12(x, y, p, q, f, x1, y1)
    # print(eqs[0])
    # we = sym.nsolve((eqs[0]), (y), -1)
    print(we)
    # calc =  CalculationPoint(f, u)