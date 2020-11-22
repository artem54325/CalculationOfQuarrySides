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

        answer = sym.nsolve([calc12Plus, calc12minus, calc14minus, calc14plus], [x, y, p, q], [((a+n)/2), ((b+m)/2), ((c+g)/2), ((d+h)/2-0.1)], verify=False)


        return Point(round(answer[0], 5), round(answer[1], 5), round(answer[2], 5), round(answer[3], 5))

    def calcSymbExample(self, Point1, Point2):
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

        answer = sym.nsolve([calc12Plus, calc12minus, calc14minus, calc14plus], [x, y, p, q], [9, -0.836, 1.913, 0.9])


        return Point(round(answer[0], 5), round(answer[1], 5), round(answer[2], 5), round(answer[3], 5))

    def calcSymbWithAngle(self, Point1, Point2):
        x = sym.Symbol('x')
        y = sym.Symbol('y')
        p = sym.Symbol('p')
        q = sym.Symbol('q')
        alpha = sym.Symbol('alpha')
        betta = sym.Symbol('betta')

        # x = -0.475
        # y = -1.568
        # p = 2.115
        # q = 0.832
        # alpha = 6.015
        # betta = 1.785

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

        # print((((f-2*p)*(1-q*q)**(1/2)+2*(f*f*q*q*(1-q*q)+p*(p-f))**(1/2))/((f-p)*(1-q*q)**(1/2))))
        # print((u*(y-b)*(2*p+(q-1)*f)/((f-p)*p)))
        # print((u*(x-a)*((q*q-1)*f)/(p*(f-p)*(1-q*q)**(1/2))))
        # print((((2*p-f*(1+2*q))/(f-p))*(q-d) + (((f-2*p)*(1-q*q)**(1/2)+2*(f*f*q*q*(1-q*q)+p*(p-f))**(1/2))/((f-p)*(1-q*q)**(1/2)))*(q-d) +
        #          (u*(y-b)*(2*p+(q-1)*f)/((f-p)*p)) + (u*(x-a)*((q*q-1)*f)/(p*(f-p)*(1-q*q)**(1/2)))))
        #
        # print((1 + (f * ((p * p - 1) / f)))**(1/2))
        # print(p, f)
        # print(((p * p - 1) / f), 6.016)
        # print(((p * p - 1) / f - 2 * p), 1.786)

        # Первое уравнение
        calc1 = sym.cos(2 * (-1) * sym.atan((x - n) / (y - m))) - q

        # Второе уравнение
        calc2 = (x-a) * (((f-2*p) * ((1-q*q)**(1/2))+2*((f*f*q*q*(1-q*q)+p*(p-f))**(1/2)))/(2*f*q*q+(2*p-f)*q-f))-(y-b)

        # Средняя уравнение
        calc3 = (((2*p-f*(1+2*q))/(f-p))*(q-d) + (((f-2*p)*(1-q*q)**(1/2)+2*(f*f*q*q*(1-q*q)+p*(p-f))**(1/2))/((f-p)*(1-q*q)**(1/2)))*(q-d) +
                 (u*(y-b)*(2*p+(q-1)*f)/((f-p)*p)) + (u*(x-a)*((q*q-1)*f)/(p*(f-p)*(1-q*q)**(1/2)))-(4*(p-c)/f))

        # Четвертое уравнение
        calc4 = (1 + (f * alpha))**(1/2) - p    #(1 + (f * ((p * p-1) / f)) / 1)**(1/2) - p # (1+(f*((p*p-1)/f)))

        calc5 = ((p * p - 1) / f) - alpha

        calc6 = ((p * p - 1) / f - 2 * p) - betta


        answer = sym.nsolve([calc1, calc2, calc3, calc4, calc5, calc6], [x, y, p, q, alpha, betta], [-0.476, -1.568, 2.115, 0.831, 6.015, 1.785])
        print(round(answer[0], 5), round(answer[1], 5), round(answer[2], 5), round(answer[3], 5))
        return Point(round(answer[0], 5), round(answer[1], 5), round(answer[2], 5), round(answer[3], 5))



if __name__ == "__main__":
    m = Mathcad()
    length = 5

    points = [Point(1, -0.836, 1.913, 1), Point(0, 0, 1.732, 1)]
    # points = [Point(-0.315, -5.418, 2.747, 0.678), Point(-1.778, -4.729, 2.602, 0.76)]
    # points = [Point(10, 0.0, 1.732, 1),
    #           Point(8, 0.0, 1.732, 1)]
    check = m.calcSymbWithAngle(points[0], points[1])
    # print(check)

    # add mass
    # mass = []
    # mass.append([])
    # for i in range(0, length):
    #     mass[0].append(Point(i*2, 0,1.732, 1))
    # # calculations
    # for i in range(0, length):
    #     mass.append([])
    #     for idx, point in enumerate(mass[i]):
    #         if(idx + 1 >= len(mass[i])):
    #             continue
    #         # print(mass[i][idx+1], point)
    #         res = m.calcSymb(mass[i][idx+1], point)
    #         if(res != None):
    #             mass[i+1].append(res)
    #
    # for idx, point in enumerate(mass):
    #     print(point)