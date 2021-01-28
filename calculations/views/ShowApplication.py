import threading
import wx
import wx.grid
from calculations.plasticityCriterion.CalcukationsMathcad2 import Mathcad
import math
from models.Point import Point
from calculations.views.ShowTable import ShowTable


class ShowApplication(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(
            self, None, size=(680, 250), title='Расчет бортов карьеров на обрушения'
        )
        panel = wx.Panel(self)
        self.colLabels = ["x", "y", "p", "q"]

        self.grid = wx.grid.Grid(panel, 6)
        self.grid.CreateGrid(7, 4)

        self.button = wx.Button(panel, label="Расчет")
        self.lblAgle = wx.StaticText(panel, label="Угол:")
        self.lblU = wx.StaticText(panel, label="Объемный вес:")
        self.lblС = wx.StaticText(panel, label="Сцепление:")
        self.lblStep = wx.StaticText(panel, label="Шаг для расчета:")
        self.lblLength = wx.StaticText(panel, label="Длина для расчета:")
        self.lblTable = wx.StaticText(panel, label="Заполнение крайних точек")

        self.editAgle = wx.TextCtrl(panel, size=(140, -1))
        self.editU = wx.TextCtrl(panel, size=(140, -1))
        self.editC = wx.TextCtrl(panel, size=(140, -1))
        self.editStep = wx.TextCtrl(panel, size=(140, -1))
        self.editLength = wx.TextCtrl(panel, size=(140, -1))

        self.sizer = wx.GridBagSizer(6, 1)
        self.sizer.Add(self.lblAgle, (0, 0))
        self.sizer.Add(self.editAgle, (0, 1))
        self.sizer.Add(self.lblU, (1, 0))
        self.sizer.Add(self.editU, (1, 1))
        self.sizer.Add(self.lblС, (2, 0))
        self.sizer.Add(self.editC, (2, 1))
        self.sizer.Add(self.lblStep, (3, 0))
        self.sizer.Add(self.editStep, (3, 1))
        self.sizer.Add(self.lblLength, (4, 0))
        self.sizer.Add(self.editLength, (4, 1))
        self.sizer.Add(self.button, (5, 0), (0, 2), flag=wx.EXPAND)
        self.sizer.Add(self.lblTable, (0,4), (0,3))
        self.sizer.Add(self.grid, (1,3), (6,4))

        panel.SetSizer(self.sizer)

        # Set Binds
        self.button.Bind(wx.EVT_BUTTON, self.calculation)

        # Set values
        self.editAgle.SetValue("30")
        self.editU.SetValue("1")
        self.editC.SetValue("1")
        self.editStep.SetValue("2")
        self.editLength.SetValue("8")
        self.fillTable()

        self.Show()

    def changeLength(self, id):
        print(id)

    def fillTable(self):
        pointsFind = [Point(-0.475, -1.568, 2.115, 0.831, 6.015, 1.785),
                      Point(-1.186, -3.128, 2.421, 0.655, 8.422, 3.58),
                      Point(-1.778, -4.729, 2.02, 0.76, 9.998, 4.793),
                      Point(-2.241, -6.363, 2.767, 0.851, 11.528, 5.994)]
        # self.grid.SetCel
        for i, point in enumerate(pointsFind):
            self.grid.SetCellValue(i, 0, str(point.getX()))
            self.grid.SetCellValue(i, 1, str(point.getY()))
            self.grid.SetCellValue(i, 2, str(point.getP()))
            self.grid.SetCellValue(i, 3, str(point.getQ()))
            # https://stackoverflow.com/questions/17454775/changing-size-of-grid-when-grid-data-is-changed

    def getTable(self):
        pointsFind = [Point(-0.475, -1.568, 2.115, 0.831, 6.015, 1.785),
                      Point(-1.186, -3.128, 2.421, 0.655, 8.422, 3.58),
                      Point(-1.778, -4.729, 2.02, 0.76, 9.998, 4.793),
                      Point(-2.241, -6.363, 2.767, 0.851, 11.528, 5.994)]
        q = self.grid.GetSelectedCells()
        for i, point in enumerate(pointsFind):
            self.grid.SetCellValue(i, 0, str(point.getX()))
            self.grid.SetCellValue(i, 1, str(point.getY()))
            self.grid.SetCellValue(i, 2, str(point.getP()))
            self.grid.SetCellValue(i, 3, str(point.getQ()))
        return [Point(-0.475, -1.568, 2.115, 0.831, 6.015, 1.785),
                      Point(-1.186, -3.128, 2.421, 0.655, 8.422, 3.58),
                      Point(-1.778, -4.729, 2.02, 0.76, 9.998, 4.793),
                      Point(-2.241, -6.363, 2.767, 0.851, 11.528, 5.994)]

    def calculation(self, e):
        # self.grid.AppendRows()
        print("Angle = ", self.editAgle.GetValue())
        print("U = ", self.editU.GetValue())
        print("C = ", self.editC.GetValue())
        print("Step = ", self.editStep.GetValue())
        print("Length = ", self.editLength.GetValue())

        angle = float(self.editAgle.GetValue())
        length = int(self.editLength.GetValue())
        step = float(self.editStep.GetValue())
        pointsFind = self.getTable()
        u = float(self.editU.GetValue())
        C = float(self.editC.GetValue())

        # e1 = threading.Event()
        # self.t1 = threading.Thread(target=self.calculations, args=(angle, u, C, step, length, pointsFind))
        # self.t1.start()
        # self.t1.join()
        self.calculations(angle, u, C, step, length, pointsFind)


    def calculations(self, angle, u, C, step, length, pointsFind):
        m = Mathcad(f=math.tan(angle * math.pi / 180), u=u, C=C)
        mass = []
        mass.append([])
        leftNumber = 1
        for i in range(0, length):
            mass[0].append(Point(i * step, 0, 1.732, 1))
        # calculations
        for i in range(0, length):
            mass.append([])

            if (len(mass) >= 3 & i % 2 == 1):
                m1 = mass[i][0]
                m2 = mass[i - 1][0]
                find = pointsFind[i - leftNumber]
                res = m.calcSymbWithAngle(m1, m2, find)
                mass[i + 1].append(res)
                leftNumber = leftNumber + 1

            for idx, point in enumerate(mass[i]):
                if (idx + 1 >= len(mass[i])):
                    continue
                prevPoint = mass[i][idx + 1]
                res = m.calcSymb3(prevPoint, point)
                if (res != None):
                    mass[i + 1].append(res)

        showTable = ShowTable()
        showTable.showTable(mass)


if __name__ == '__main__':
    app = wx.App(False)
    frame = ShowApplication()
    app.MainLoop()