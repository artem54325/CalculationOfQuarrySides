import math

import sympy as sym
import z3 as z3


# class CalculationPoint4:

    # def equation12_plus(self, x, y, p, q, f, x1, y1):
    #
    #     eq = (((f - 2 * p) * sym.sqrt(1 - q * q) + # Здесь менять
    #                 2 * sym.sqrt( f * f * q * q * ( 1 - q * 2 ) + p * ( p - f ))) /
    #                ( 2 * f * q * q + ( 2 * p - f) * q - f)) - ((y - y1) / (x - x1))
    #
    #
    #     return eq
    #
    # def equation14_plus(self, x, y, p, q, f, x1, y1, p1, q1):
    #     eq = (
    #             (2 * p - f * (1 + 2 * q)) * (q - q1) / (f - p) +
    #             ((self.equation12_plus(x, y, p, q, f, x1, y1)) * (2 * p * q - f * q + 2 * f * q * q - f) / (sym.sqrt(1 + q * q) * f - p)) * (
    #                         q - q1) +
    #             u * (y - y1) * (2 * p + f * (q - 1)) / (p * (f - p)) +
    #             u * (x - x1) * (f * (q * q - 1)) / (sym.sqrt(1 + q * q) * p * (f - p)) -
    #             4 * 1 / f * (p - p1)  # left side
    #     )
    #     return  eq
    #
    # def equation12_minus(self, x, y, p, q, f, x1, y1):
    #
    #     eq = (((f - 2 * p) * sym.sqrt(1 - q * q) - # Здесь менять
    #                 2 * sym.sqrt( f * f * q * q * ( 1 - q * 2 ) + p * ( p - f ))) /
    #                ( 2 * f * q * q + ( 2 * p - f) * q - f)) - ((y - y1) / (x - x1))
    #
    #
    #     return eq
    #
    # def equation14_minus(self, x, y, p, q, f, x1, y1, p1, q1):
    #     eq = (
    #             (2 * p - f * (1 + 2 * q)) * (q - q1) / (f - p) +
    #             ((self.equation12_plus(x, y, p, q, f, x1, y1)) * (2 * p * q - f * q + 2 * f * q * q - f) / (sym.sqrt(1 + q * q) * f - p)) * (
    #                         q - q1) +
    #             u * (y - y1) * (2 * p + f * (q - 1)) / (p * (f - p)) +
    #             u * (x - x1) * (f * (q * q - 1)) / (sym.sqrt(1 + q * q) * p * (f - p)) -
    #             4 * 1 / f * (p - p1)  # left side
    #     )
    #     return  eq
    #
    #
    # def equation14(self, x, y, p, q, f, u, x1, y1, p1, q1):
    #
    #     eq = (
    #             (2 * p - f * (1 + 2 * q))*(q - q1)/(f - p) +
    #             (((y-y1)/(x-x1))*(2 * p * q - f * q + 2 * f * q * q - f) / (sym.sqrt(1 + q * q) * f - p)) * ( q - q1) +
    #             u * (y - y1) * (2 * p + f * (q - 1))/(p * (f - p)) +
    #             u * (x - x1) * (f * (q * q - 1))/(sym.sqrt(1 + q * q) * p * (f - p)) -
    #             4 * 1 / f * (p - p1)    # left side
    #             )
    #
    #     return eq


if __name__ == "__main__":
    # u - объемный вес
    # f - коэффициент внутреннего трения
    # calc = CalculationPoint3()
    u = 1
    f = math.tan(math.radians(30))

    # p = sym.Symbol('p')
    # q = sym.Symbol('q')
    # x = sym.Symbol('x')
    # y = sym.Symbol('y')

    p = z3.BitVec('p', 4)
    q = z3.BitVec('q', 4)
    x = z3.BitVec('x', 4)
    y = z3.BitVec('y', 4)

    # p = 1.732
    # q = 1
    p1 = 1.732
    q1 = 1
    p2 = 1.732
    q2 = 1
    x1 = 0
    y1 = 0
    x2 = 2
    y2 = 0
    solver = z3.Solver()
    constants =[
        ((y - y2) / (x - x2)) ==(
            ((f - 2 * p) * z3.Sqrt(1 - q * q) +
             2 * z3.Sqrt(f * f * q * q * (1 - q * q) + p * (p - f))) /
            (2 * f * q * q + (2 * p - f) * q - f)
        ),
        ((y - y1) / (x - x1)) == (
                ((f - 2 * p) * z3.Sqrt(1 - q * q) -
                 2 * z3.Sqrt(f * f * q * q * (1 - q * q) + p * (p - f))) /
                (2 * f * q * q + (2 * p - f) * q - f)
        ),
        4 * 1 / f * (p - p1)  == (2 * p - f * (1 + 2 * q)) * (q - q1) / (f - p) +
                    (((y - y1) / (x - x1))*(2 * p * q - f * q + 2 * f * q * q - f)
                     / (z3.Sqrt(1 + q * q) * f - p)) * ( q - q1) +
                    u * (y - y1) * (2 * p + f * (q - 1))/(p * (f - p)) +
                    u * (x - x1) * (f * (q * q - 1))/(z3.Sqrt(1 + q * q) * p * (f - p)),

        4 * 1 / f * (p - p1) == (2 * p - f * (1 + 2 * q)) * (q - q1) / (f - p) +
                    (((y - y2) / (x - x2)) * (2 * p * q - f * q + 2 * f * q * q - f)
                     / (z3.Sqrt(1 + q * q) * f - p)) * (q - q1) +
                    u * (y - y2) * (2 * p + f * (q - 1)) / (p * (f - p)) +
                    u * (x - x2) * (f * (q * q - 1)) / (z3.Sqrt(1 + q * q) * p * (f - p))
    ]
    for i in constants:
        solver.add(i)
    while solver.check() == z3.sat:
        print(solver.model()[x], solver.model()[y])
        solver.add(x != solver.model()[x],
                   y != solver.model()[y])
        # добавляем условия, что новое решение на равно найденному
    # eq = sym.solve({calc.equation12_minus(x, y, p, q, f, x1, y1).subs('p', 1.732).subs('q', 1),
    #                 calc.equation14_minus(x, y, p, q, f, x1, y1, p1, q1).subs('p', 1.732).subs('q', 1) },{x,y}, -1)
    # eq = sym.solve({calc.equation12_minus(x, y, p, q, f, x1, y1), calc.equation14_minus(x, y, p, q, f, x1, y1, p1, q1),
    #                  calc.equation12_plus(x, y, p, q, f, x2, y2), calc.equation14_plus(x, y, p, q, f, x2, y2, p2, q2)}, {p, q, x, y}, -1)

    # eq = sym.solve({calc.equation12_minus(x, y, p, q, f, x1, y1), calc.equation14_minus(x, y, p, q, f, x1, y1, p1, q1),
    #                 calc.equation12_plus(x, y, p, q, f, x2, y2), calc.equation14_plus(x, y, p, q, f, x2, y2, p2, q2)},
    #                {q, x, y}
    #                )
    # print(eq)