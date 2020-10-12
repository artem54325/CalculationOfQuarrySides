import math

import sympy as sym
import z3 as z3

class Mathcad:
    def __init__(self):
        self.a = 2
        self.b = 0
        self.c = 1.732
        self.d = 1

        self.n = 0
        self.m = 0
        self.g = 1.732
        self.h = 1

        self.exX = -1
        self.exY = -0.8
        self.exP = 1.9
        self.exQ = 0.9

    def calc(self):
        x = z3.BitVec('x', 4)
        y = z3.BitVec('y', 4)
        p = z3.BitVec('p', 4)
        q = z3.BitVec('q', 4)

        f = 0.577
        C = 1
        u =1

        a = self.a
        b = self.b
        c = self.c
        d = self.d

        n = self.n
        m = self.m
        g = self.g
        h = self.h
        # ((y - y2) / (x - x2)) == (
        #         ((f - 2 * p) * z3.Sqrt(1 - q * q) +
        #          2 * z3.Sqrt(f * f * q * q * (1 - q * q) + p * (p - f))) /
        #         (2 * f * q * q + (2 * p - f) * q - f)
        # )
        solver = z3.Solver()
        constants = [
            y - b == (x - a) * (((f - 2 * p) * z3.Sqrt(1 - q * q) +
                                 (2 * z3.Sqrt(f * f * q * q * (1 - q * q) + p * (p - f)))) /
                                (2 * f * q * q + (2 * p - f) * q - f)),

            y - m == (x - n) * (((f - 2 * p) * z3.Sqrt(1 - q * q) -
                                 (2 * z3.Sqrt(f * f * q * q * (1 - q * q) + p * (p - f)))) /
                                (2 * f * q * q + (2 * p - f) * q - f)),


            (4 * (p - c)) / (f) == ((2 * p - f * (1 + 2 * q)) / (f - p) * (q - d) +
                                    ((f - 2 * p) * z3.Sqrt(1 - q * q) + 2 * z3.Sqrt(
                                        f * f * q * q * (1 - q * q) + p * (p - f))) /
                                    (1 * (f - p) * (z3.Sqrt(1 - q * q))) * (q - d) +
                                    (u * (y - b) * (2 * p + (q - 1) * f)) / ((f - p) * p) +
                                    (u * (x - a) * (q * q - 1) * f) / (1 * p * (f - p) * z3.Sqrt(1 - q * q))),

            (4 * (p - g)) / (f) == ((2 * p - f * (1 + 2 * q)) / (f - p) * (q - h) +
                                    ((f - 2 * p) * z3.Sqrt(1 - q * q) - 2 * z3.Sqrt(
                                        f * f * q * q * (1 - q * q) + p * (p - f))) /
                                    (1 * (f - p) * (z3.Sqrt(1 - q * q))) * (q - h) +
                                    (u * (y - b) * (2 * p + (q - 1) * f)) / ((f - p) * p) +
                                    (u * (x - a) * (q * q - 1) * f) / (1 * p * (f - p) * z3.Sqrt(1 - q * q)))
        ]
        for i in constants:
            solver.add(i)
        while solver.check() == z3.sat:
            print(solver.model()[x], solver.model()[y])
            solver.add(x != solver.model()[x],
                       y != solver.model()[y])

    def calcSymb(self):
        x = sym.Symbol('x')
        y = sym.Symbol('y')
        p = sym.Symbol('p')
        q = sym.Symbol('q')

        f = 0.577
        c = 1
        u = 1

        a = self.a
        b = self.b
        c = self.c
        d = self.d

        n = self.n
        m = self.m
        g = self.g
        h = self.h
        # ((y - y2) / (x - x2)) == (
        #         ((f - 2 * p) * z3.Sqrt(1 - q * q) +
        #          2 * z3.Sqrt(f * f * q * q * (1 - q * q) + p * (p - f))) /
        #         (2 * f * q * q + (2 * p - f) * q - f)
        # )

        calc12Plus = (x - a) * (((f - 2 * p) * (1 - q * q)**(1/2) +
                                 (2 * (f * f * q * q * (1 - q * q) + p * (p - f))**(1/2))) /
                                (2 * f * q * q + (2 * p - f) * q - f)) - (y - b)

        calc12minus = (x - n) * (((f - 2 * p) * (1 - q * q)**(1/2) -
                                 (2 * (f * f * q * q * (1 - q * q) + p * (p - f))**(1/2))) /
                                (2 * f * q * q + (2 * p - f) * q - f)) - (y - m)

        calc14minus = ((2 * p - f * (1 + 2 * q)) / (f - p) * (q - d) +
                                    ((f - 2 * p) * (1 - q * q)**(1/2) + 2 *
                                     (f * f * q * q * (1 - q * q) + p * (p - f))**(1/2)) /
                                    (1 * (f - p) * ((1 - q * q)**(1/2))) * (q - d) +
                                    (u * (y - b) * (2 * p + (q - 1) * f)) / ((f - p) * p) +
                                    (u * (x - a) * (q * q - 1) * f) / (1 * p * (f - p) * (1 - q * q)**(1/2))) - ((4 * (p - c)) / (f))

        calc14plus = ((2 * p - f * (1 + 2 * q)) / (f - p) * (q - h) +
                                    ((f - 2 * p) * (1 - q * q)**(1/2) - 2 *
                                    (f * f * q * q * (1 - q * q) + p * (p - f))**(1/2)) /
                                    (1 * (f - p) * ((1 - q * q)**(1/2))) * (q - h) +
                                    (u * (y - b) * (2 * p + (q - 1) * f)) / ((f - p) * p) +
                                    (u * (x - a) * (q * q - 1) * f) / (1 * p * (f - p) * (1 - q * q)**(1/2))) - ((4 * (p - g)) / (f))

        # answer = sym.nsolve([calc12Plus, calc12minus, calc14minus, calc14plus], [x, y, p, q], 0)

        print('calculations')
        answer = sym.solve((calc12Plus, calc12minus, calc14minus, calc14plus), x, y, p, q, -1)
        print(answer)
        print('answer-1')

        answer = sym.nsolve((calc12Plus, calc12minus, calc14minus, calc14plus), x, y, p, q, -1)
        print(answer)
        print('answer-2')


if __name__ == "__main__":
    m = Mathcad()
    m.calcSymb()
