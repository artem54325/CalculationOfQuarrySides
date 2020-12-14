
import numpy as np
import matplotlib.pyplot as plt
import mplcursors


class ShowTable:
    def showTable(self, massPoints):
        # https://pyprog.pro/mpl/mpl_scatter.html
        # https://plotly.com/python/line-and-scatter/

        # x - координаты точек
        # y - координаты точек
        x = []
        y = []
        for idPoints, points in enumerate(massPoints):
            for id, point in enumerate(points):
                x.append(idPoints)
                y.append(id)
                point.setTable(idPoints,id)
                # x.append(point.getX())
                # y.append(point.getY())

        fig, ax = plt.subplots()

        ax.scatter(x, y,
                  c='#ad09a3')  # цвет точек

        ax.set_title('Расчет бортов карьеров на обрушения')  # заголовок для Axes

        fig.set_figwidth(8)  # ширина и
        fig.set_figheight(8)  # высота "Figure"

        crs = mplcursors.cursor(ax, hover=True)

        crs.connect("add", lambda sel: sel.annotation.set_text(
            self.searchPoint(massPoints, sel.target[1], sel.target[0])))#'Point {},{}'.format(sel.target[0], sel.target[1])

        plt.show()

    def searchPoint(self, massPoints, y, x):
        for idPoints, points in enumerate(massPoints):
            for id, point in enumerate(points):
                # if(x == point.getX() and y == point.getY()):
                #     return point
                if (x == point.tableX and y == point.tableY):
                    return point