import math

import sympy as sym
import z3 as z3

from calculations.views.ShowTable import ShowTable
from models.Point import Point
from scipy.optimize import fsolve


class Mathcad:

    def __init__(self, f=0.577, u=1):
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

        #   fsolve AND sym.nsolve

        answer = sym.nsolve([calc12Plus, calc12minus, calc14minus, calc14plus], [x, y, p, q], [((a+n)/2), ((b+m)/2), ((c+g)/2), ((d+h)/2-0.1)], verify=False)

        answer2 = fsolve(self.calculation,
                        [((a + n) / 2), ((b + m) / 2), ((c + g) / 2), ((d + h) / 2 - 0.1)], args=[Point1, Point2])

        print('\n', answer, '\n',answer2)

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


    def calcSymbWithAngle(self, Point1, Point2):
        x = sym.Symbol('x')
        y = sym.Symbol('y')
        p = sym.Symbol('p')
        q = sym.Symbol('q')
        alpha = sym.Symbol('alpha')
        betta = sym.Symbol('betta')

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

        print((Point1.getX()+Point2.getX())/2, (Point1.getY()+Point2.getY())/2,(Point1.getP()+Point2.getP())/2,(Point1.getQ()+Point2.getQ())/2,
                             (Point1.getAlpha(f)+Point2.getAlpha(f))/2,(Point1.getBetta(f)+Point2.getBetta(f))/2)

        # pointExample = Point(-0.476, -1.568, 2.115, 0.831, 6.015, 1.785)
        pointExample = Point((Point1.getX()+Point2.getX())/2, (Point1.getY()+Point2.getY())/2,(Point1.getP()+Point2.getP())/2,(Point1.getQ()+Point2.getQ())/3,
                             (Point1.getAlpha(f)+Point2.getAlpha(f))/2,(Point1.getBetta(f)+Point2.getBetta(f))/2)
        print(pointExample)

        # answer = sym.solve([calc1, calc2, calc3, calc4, calc5, calc6],
        #                     x, y, p, q, alpha, betta,
        #                     dist=True)
                            # [-0.476, -1.568, 2.115, 0.831, 6.015, 1.785])
                            # [pointExample.getX(), pointExample.getY(), pointExample.getP(), pointExample.getQ()
                            #  , pointExample.getAlpha(f), pointExample.getBetta(f)],
                            # [(Point1.getX()+Point2.getX())/2, (Point1.getY()+Point2.getY())/2,(Point1.getP()+Point2.getP())/2,(Point1.getQ()+Point2.getQ())/2 -0.01,
                            #  (Point1.getAlpha(f)+Point2.getAlpha(f))/2,(Point1.getBetta(f)+Point2.getBetta(f))/2])
        try:
            answer = sym.nsolve([calc1, calc2, calc3, calc4],
                                [x, y, p, q],
                                # [-0.5, -1.5, 2.1,
                                #  0.8, 6.0, 1.7],
                                [pointExample.getX(), pointExample.getY(), pointExample.getP(), pointExample.getQ()],
                                # [-pointExample.getX(), pointExample.getY(), pointExample.getP(),
                                #  pointExample.getQ(), pointExample.getAlpha(f), pointExample.getBetta(f)],
                                simplify=False, rational=False, solution_dict=False, verify=False)
            print(answer)
        except Exception:
            print("Ошибка выполнения")


        print('\n',round(answer[0], 5), round(answer[1], 5), round(answer[2], 5), round(answer[3], 5),
              '\n',' = ','\n', -0.47362, -1.56903, 2.11470, 0.83298, 6.01723, 1.78783)
        # print('\n',round(answer[0], 5), round(answer[1], 5), round(answer[2], 5), round(answer[3], 5),
        #       round(answer[4], 5), round(answer[5], 5),'\n',' = ','\n', -0.47362, -1.56903, 2.11470, 0.83298, 6.01723, 1.78783)
        # return Point(round(answer[0], 5), round(answer[1], 5), round(answer[2], 5), round(answer[3], 5))





if __name__ == "__main__":
    m = Mathcad()
    length = 8

    # points = [Point(-0.315, -5.418, 2.747, 0.678), Point(-1.778, -4.729, 2.602, 0.76)]
    # points = [Point(10, 0.0, 1.732, 1),
    #           Point(8, 0.0, 1.732, 1)]
    # points = [Point(1, -0.836, 1.913, 1), Point(0, 0, 1.732, 1)]
    points = [Point(-0.475, -1.568, 2.115, 0.832, 6.015, 1.785), Point(0.129, -2.622, 2.296, 0.833,7.399, 2.807)]
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
    # showTable = ShowTable()
    # showTable.showTable(mass)