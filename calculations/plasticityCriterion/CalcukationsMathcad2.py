import math

import numpy
import sympy as sym
import z3 as z3

from calculations.views.ShowTable import ShowTable
from models.Point import Point
from helpers import parsFloat


class Mathcad:

    def __init__(self, f=math.tan(30*math.pi/180), u=1):
        self.f = f
        self.u = u

    def calcSymb(self, Point1, Point2):
        x = sym.Symbol('x')
        y = sym.Symbol('y')
        p = sym.Symbol('p')
        q = sym.Symbol('q')

        f = self.f
        u = self.u

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

        answer = sym.nsolve([calc12Plus, calc12minus, calc14minus, calc14plus],
                            [x, y, p, q],
                            [((a+n)/2), ((b+m)/2), ((c+g)/2), ((d+h)/2-0.1)],
                            # [0.129, -2.622, 2.296, 0.833],
                            verify = True)

        return Point(round(answer[0], 5), round(answer[1], 5), round(answer[2], 5), round(answer[3], 5))

    def calculation(self, qiq, points):
        Point1 = points[0]
        Point2 = points[0]

        x = qiq[0]
        y = qiq[1]
        p = qiq[2]
        q = qiq[3]

        f = self.f
        u = self.u

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

        return (calc12Plus, calc12minus, calc14minus, calc14plus)

    def calculationAngle(self, qiq, points):
        Point1 = points[0]
        Point2 = points[0]

        x = qiq[0]
        y = qiq[1]
        p = qiq[2]
        q = qiq[3]

        f = self.f
        u = self.u

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

        return (calc12Plus, calc12minus, calc14minus, calc14plus)

    def calcSymbWithAngle(self, Point1, Point2, pointFind):
        x = sym.Symbol('x')
        y = sym.Symbol('y')
        p = sym.Symbol('p')
        q = sym.Symbol('q')
        alpha = sym.Symbol('alpha')
        betta = sym.Symbol('betta')

        f = self.f
        u = self.u

        a = round(float(Point1.getX()),4)# Point1.getX()
        b = round(float(Point1.getY()),4)# Point1.getY()
        c = round(float(Point1.getP()),4)# Point1.getP()
        d = round(float(Point1.getQ()),4)# Point1.getQ()

        n = round(float(Point2.getX()),4)# Point2.getX()
        m = round(float(Point2.getY()),4)# Point2.getY()
        g = round(float(Point2.getP()),4)# Point2.getP()
        h = round(float(Point2.getQ()),4)# Point2.getQ()


        # Первое уравнение
        calc1 = sym.cos(-2 * sym.atan((x - n) / (y - m))) - q

        # Второе уравнение
        calc2 = ((x-a) * (((f-2*p) * ((1-q*q)**(1/2))+
                           2*((f*f*q*q*(1-q*q)+p*(p-f))**(1/2)))/
                          (2*f*q*q+(2*p-f)*q-f))-(y-b))

        # Средняя уравнение
        calc3 = (((2 * p - f * (1 + 2 * q))/(f - p))*(q - d) +
                 (((f - 2 * p)*(1 - q * q)**(1/2) + 2 * (f * f * q * q * (1 - q * q) + p * (p - f))**(1/2))/((f - p)*(1 - q * q)**(1/2)))*(q - d) +
                 (u * (y - b)*(2 * p + (q - 1) * f)/((f - p) * p)) +
                 (u * (x - a)*((q * q -1) * f)/(p * (f - p)*(1 - q * q)**(1/2))) -
                 (4 * (p - c) / f))

        # Четвертое уравнение
        calc4 = (1 + (f * alpha))**(1/2) - p

        # Пятое уравнение
        calc5 = ((p * p - 1) / f) - alpha

        # Шестое уравнение
        calc6 = (alpha - 2 * p) - betta

        answer = sym.nsolve([calc1, calc2, calc3, calc4, calc5, calc6],
                            [x, y, p, q, alpha, betta],
                            # [((a+n)/2), ((b+m)/2), ((c+g)/2), ((d+h)/2-0.1), ((Point1.getAlpha(f)+Point2.getAlpha(f))/2-0.1), ((Point1.getBetta(f)+Point2.getBetta(f))/2-0.1)],
                            [pointFind.getX(), pointFind.getY(), pointFind.getP(),pointFind.getQ(),pointFind.getAlpha(f),pointFind.getBetta(f)],
                            verify = False)
        # answer = numpy.ndarray(answer, dtype=float, order='F')
        return Point(round(parsFloat(answer[0]), 5), round(parsFloat(answer[1]), 5), round(parsFloat(answer[2]), 5), round(parsFloat(answer[3]), 5))


    def calcSymb2(self, Point1, Point2):
        #0.129, -2.622, 2.296, 0.833
        x = sym.Symbol('x')
        y = sym.Symbol('y')
        p = sym.Symbol('p')
        q = sym.Symbol('q')

        f = self.f
        u = self.u

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

        calc14plus = (((2 * p - f * (1 + 2 * q)) / (f - p)) * (q - d) +

                                    ((f - 2 * p) * (1 - q * q)**(1/2) +
                                     2 * ((f * f * q * q * (1 - q * q) + p * (p - f))**(1/2)) /
                                    ((f - p) * ((1 - q * q)**(1/2)))) * (q - d) +

                                    (u * (y - b) * (2 * p + (q - 1) * f)) / ((f - p) * p) +

                                    (u * (x - a) * (q * q - 1) * f) / (p * (f - p) * (1 - q * q)**(1/2))) - ((4 * (p - c)) / f)


        calc14minus = (((2 * p - f * (1 + 2 * q)) / (f - p)) * (q - h) +

                                    ((f - 2 * p) * (1 - q * q)**(1/2) -
                                     2 * (f * f * q * q * (1 - q * q) + p * (p - f))**(1/2)) /
                                    ((f - p) * ((1 - q * q)**(1/2))) * (q - h) +

                                    (u * (y - m) * (2 * p + (q - 1) * f)) / ((f - p) * p) +

                                    (u * (x - n) * (q * q - 1) * f) / (p * (f - p) * (1 - q * q)**(1/2))) - ((4 * (p - g)) / f)


        answer = sym.nsolve([calc12Plus, calc12minus, calc14minus, calc14plus],
                            [x, y, p, q],
                            [((a+n)/2), ((b+m)/2), ((c+g)/2), ((d+h)/2-0.1)],
                            verify = False)

        return Point(round(parsFloat(answer[0]), 5), round(parsFloat(answer[1]), 5), round(parsFloat(answer[2]), 5), round(parsFloat(answer[3]), 5))

    def calcSymb3(self, Point1, Point2):
        x = sym.Symbol('x')#0.129#sym.Symbol('x')
        y = sym.Symbol('y')#-2.622#sym.Symbol('y')
        p = sym.Symbol('p')#2.296#sym.Symbol('p')
        q = sym.Symbol('q')#0.833#sym.Symbol('q')

        f = self.f
        u = self.u

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


        calc14plus = ((2 * p - f * (1 + 2 * q)) / (f - p) * (q - d) +

                    ((f - 2 * p) * (1 - q * q)**(1/2) +
                     2 * (f * f * q * q * (1 - q * q) + p * (p - f))**(1/2)) /
                    (1 * (f - p) * ((1 - q * q)**(1/2))) * (q - d) +

                    (u * (y - b) * (2 * p + (q - 1) * f)) / ((f - p) * p) +

                    (u * (x - a) * (q * q - 1) * f) / (1 * p * (f - p) * (1 - q * q)**(1/2)) -

                    ((4 * (p - c)) / (f)))


        calc14minus = ((((2 * p - f * (1 + 2 * q)) / (f - p)) * (q - h) +

                    ((f - 2 * p) * (1 - q * q)**(1/2) -
                     2 * (f * f * q * q * (1 - q * q) + p * (p - f))**(1/2)) /
                    (1 * (f - p) * ((1 - q * q)**(1/2))) * (q - h) +

                    (u * (y - m) * (2 * p + (q - 1) * f)) / ((f - p) * p) +

                    (u * (x - n) * (q * q - 1) * f) / (1 * p * (f - p) * (1 - q * q)**(1/2))) -

                    ((4 * (p - g)) / f))

        answer = sym.nsolve([calc12Plus, calc12minus, calc14minus, calc14plus],
                            [x, y, p, q],
                            [((a+n)/2), ((b+m)/2), ((c+g)/2), ((d+h)/2-0.1)],
                            # [0.129, -2.622, 2.296, 0.833],
                            verify = False)

        return Point(round(parsFloat(answer[0]), 5), round(parsFloat(answer[1]), 5), round(parsFloat(answer[2]), 5), round(parsFloat(answer[3]), 5))

if __name__ == "__main__":
    m = Mathcad()
    length = 6
    pointsFind = [Point(-0.475, -1.568, 2.115, 0.831, 6.015, 1.785),
                  Point(-1.186, -3.128, 2.421, 0.655, 8.422, 3.58),
                  Point(-1.778, -4.729, 2.02, 0.76, 9.998, 4.793),
                  Point(-2.241, -6.363, 2.767, 0.851, 11.528, 5.994)]

    #Test
    # points2 = [Point(0.0, 0.0, 1.732, 1), Point(1, -0.836, 1.913, 1)]
    # pw = pointsFind[0]
    # answer2 = m.calcSymbWithAngle(points2[1], points2[0], pw)
    # print('\n', answer2,'\n', pw)
    #
    # points2 = [Point(-0.475, -1.568, 2.115, 0.832), Point(0.129, -2.622, 2.296, 0.833)]
    # pw = pointsFind[1]
    # answer2 = m.calcSymbWithAngle(points2[1], points2[0], pw)
    # print('\n', answer2,'\n', pw)
    #
    # points2 = [Point(-1.186, -3.128, 2.421, 0.655), Point(-0.757, -4.271, 2.59, 0.668)]
    # pw = pointsFind[2]
    # answer2 = m.calcSymbWithAngle(points2[1], points2[0], pw)
    # print('\n', answer2,'\n', pw)
    #
    # points2 = [Point(-1.778, -4.729, 2.6025, 0.76), Point(-1.246, -5.841, 2.754, 0.766)]
    # pw = pointsFind[3]
    # answer2 = m.calcSymbWithAngle(points2[1], points2[0], pw)
    # print('\n', answer2,'\n', pw)

    # m1 = {Point} <x:0.116 y:-2.6223 p:2.2972 q:0.8287 a1:7.4127 a2:2.8183>
    # m2 = {Point} <x:-0.4826 y:-1.5652 p:2.115 q:0.8264 a1:6.0191 a2:1.7892>
    # find = {Point} <x:-0.475 y:-1.568 p:2.115 q:0.831 a1:6.0195 a2:1.7895>

    # # points = [Point(-0.315, -5.418, 2.747, 0.678), Point(-1.778, -4.729, 2.602, 0.76)]
    # # points = [Point(10, 0.0, 1.732, 1),
    # #           Point(8, 0.0, 1.732, 1)]
    # points = [Point(1, -0.836, 1.913, 1), Point(0, 0, 1.732, 1)]
    # # # pointExample = Point(-0.476, -1.568, 2.115, 0.831, 6.015, 1.785)
    # # pointsFind = [Point(-0.476, -1.568, 2.115, 0.831, 6.015, 1.785),
    # #               Point(-1.186, -3.128, 2.421, 0.655, 8.422, 3.58),
    # #               Point(-1.778, -4.729, 2.02, 0.76, 9.998, 4.793),
    # #               Point(-2.241, -6.363, 2.767, 0.851, 11.528, 5.994)]
    # check = m.calcSymbWithAngle(points[0], points[1],pointsFind[0])
    # print(check)

    # add mass
    mass = []
    mass.append([])
    leftNumber = 1
    for i in range(0, length):
        mass[0].append(Point(i * 0.5, 0, 1.732, 1))
    # calculations
    for i in range(0, length):
        mass.append([])

        if(len(mass)>=3 & i % 2 == 1):
            m1 = mass[i][0]
            m2 = mass[i-1][0]
            # if(i>=3):
            #     m1 = pointsFind[i-leftNumber-1]
            #     m1Example = pointsFind[i-leftNumber-1] # Убрать дальше
            find = pointsFind[i-leftNumber]
            res = m.calcSymbWithAngle(m1, m2, find)
            mass[i+1].append(res)
            leftNumber = leftNumber + 1

        for idx, point in enumerate(mass[i]):
            if(idx + 1 >= len(mass[i])):
                continue
            prevPoint = mass[i][idx+1]
            res = m.calcSymb3(prevPoint, point)
            if(res != None):
                mass[i+1].append(res)

    showTable = ShowTable()
    showTable.showTable(mass)