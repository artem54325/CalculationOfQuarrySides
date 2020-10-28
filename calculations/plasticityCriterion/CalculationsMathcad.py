import math

import sympy as sym
import z3 as z3

from models.Point import Point


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
        # x = z3.Float128('x', 64)
        # y = z3.IntVector('y', 64)
        # p = z3.IntVector('p', 64)
        # q = z3.IntVector('q', 64)
        x = z3.FloatHalf('x')
        y = z3.FloatHalf('y')
        p = z3.FloatHalf('p')
        q = z3.FloatHalf('q')

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
        # constants = [
        #     y - b == (x - a) * (((f - 2 * p) * z3.Sqrt(1 - q * q) +
        #                          (2 * z3.Sqrt(f * f * q * q * (1 - q * q) + p * (p - f)))) /
        #                         (2 * f * q * q + (2 * p - f) * q - f)),
        #
        #     y - m == (x - n) * (((f - 2 * p) * z3.Sqrt(1 - q * q) -
        #                          (2 * z3.Sqrt(f * f * q * q * (1 - q * q) + p * (p - f)))) /
        #                         (2 * f * q * q + (2 * p - f) * q - f)),
        #
        #
        #     (4 * (p - c)) / (f) == ((2 * p - f * (1 + 2 * q)) / (f - p) * (q - d) +
        #                             ((f - 2 * p) * z3.Sqrt(1 - q * q) + 2 *
        #                              z3.Sqrt(f * f * q * q * (1 - q * q) + p * (p - f))) /
        #                             (1 * (f - p) * (z3.Sqrt(1 - q * q))) * (q - d) +
        #                             (u * (y - b) * (2 * p + (q - 1) * f)) / ((f - p) * p) +
        #                             (u * (x - a) * (q * q - 1) * f) / (1 * p * (f - p) * z3.Sqrt(1 - q * q))),
        #
        #     (4 * (p - g)) / (f) == ((2 * p - f * (1 + 2 * q)) / (f - p) * (q - h) +
        #                             ((f - 2 * p) * z3.Sqrt(1 - q * q) - 2 * z3.Sqrt(
        #                                 f * f * q * q * (1 - q * q) + p * (p - f))) /
        #                             (1 * (f - p) * (z3.Sqrt(1 - q * q))) * (q - h) +
        #                             (u * (y - b) * (2 * p + (q - 1) * f)) / ((f - p) * p) +
        #                             (u * (x - a) * (q * q - 1) * f) / (1 * p * (f - p) * z3.Sqrt(1 - q * q)))
        # ]
        constants = [
            y - b == (x - a) * (((f - 2 * p) * (1 - q * q)**(1/2) +
                                 (2 * (f * f * q * q * (1 - q * q) + p * (p - f))**(1/2))) /
                                (2 * f * q * q + (2 * p - f) * q - f)),

            y - m == (x - n) * (((f - 2 * p) * (1 - q * q)**(1/2) -
                                 (2 * (f * f * q * q * (1 - q * q) + p * (p - f))**(1/2))) /
                                (2 * f * q * q + (2 * p - f) * q - f)),

            (4 * (p - c)) / (f) == ((2 * p - f * (1 + 2 * q)) / (f - p) * (q - d) +
                                    ((f - 2 * p) * (1 - q * q)**(1/2) + 2 *
                                    (f * f * q * q * (1 - q * q) + p * (p - f))**(1/2)) /
                                    (1 * (f - p) * ((1 - q * q)**(1/2))) * (q - d) +
                                    (u * (y - b) * (2 * p + (q - 1) * f)) / ((f - p) * p) +
                                    (u * (x - a) * (q * q - 1) * f) / (1 * p * (f - p) * (1 - q * q)**(1/2))),

            (4 * (p - g)) / (f) == ((2 * p - f * (1 + 2 * q)) / (f - p) * (q - h) +
                                    ((f - 2 * p) * (1 - q * q)**(1/2) - 2 *
                                     (f * f * q * q * (1 - q * q) + p * (p - f))**(1/2)) /
                                    (1 * (f - p) * ((1 - q * q)**(1/2))) * (q - h) +
                                    (u * (y - b) * (2 * p + (q - 1) * f)) / ((f - p) * p) +
                                    (u * (x - a) * (q * q - 1) * f) / (1 * p * (f - p) * (1 - q * q)**(1/2)))
        ]
        for i in constants:
            solver.add(i)
        while solver.check() == z3.sat:
            print(solver.model()[x], solver.model()[y], solver.model()[p], solver.model()[q])
            solver.add(x != solver.model()[x],
                       y != solver.model()[y],
                       p != solver.model()[p],
                       q != solver.model()[q])

    def calcSymb(self, Point1, Point2):
        x = sym.Symbol('x')
        y = sym.Symbol('y')
        p = sym.Symbol('p')
        q = sym.Symbol('q')

        f = 0.577
        u = 1

        a = Point1.getX()
        b = Point1.getY()
        c = Point1.getP()
        d = Point1.getQ()

        n = Point2.getX()
        m = Point2.getY()
        g = Point2.getP()
        h = Point2.getQ()

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

        # try:
            # answer = sym.nsolve([calc12Plus, calc12minus, calc14minus, calc14plus], [x, y, p, q], [1, -1, 1.7, 0.99])
        # except Exception as e:
        #     print('Error:', Point1, Point2)
        #     return None

        answer = sym.linsolve([calc12Plus, calc12minus, calc14minus, calc14plus], x, y, p, q)


        return Point(round(answer[0], 5), round(answer[1], 5), round(answer[2], 5), round(answer[3], 5))



if __name__ == "__main__":
    m = Mathcad()
    length = 5

    # points = [Point(4, -1.685, 2.076, 1), Point(2, -1.685, 2.076, 1)]
    # points = [Point(0, 0, 1.732, 1), Point(1, -0.836, 1.913, 1)]
    # print(m.calcSymb(points[1], points[0]))

    # add mass
    mass = []
    mass.append([])
    for i in range(0, length):
        mass[0].append(Point(i * 2, 0,1.732, 1))
    #
    # calculations
    for i in range(0, length):
        mass.append([])

        for idx, point in enumerate(mass[i]):
            if(idx + 1 >= len(mass[i])):
                continue
            print(mass[i][idx+1], point)
            res = m.calcSymb(mass[i][idx+1], point)
            if(res != None):
                mass[i+1].append(res)
    print('result =',  mass)
