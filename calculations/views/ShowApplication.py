import platform
import wx


class ShowApplication(wx.Frame):

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(
            self, None, size=(360, 150), title='Расчет бортов карьеров на обрушения'
        )
        panel = wx.Panel(self)

        self.button = wx.Button(panel, label="Расчет")
        self.lblAgle = wx.StaticText(panel, label="Угол:")
        self.lblU = wx.StaticText(panel, label="Объемный вес:")
        self.lblС = wx.StaticText(panel, label="Сцепление:")

        self.editAgle = wx.TextCtrl(panel, size=(140, -1))
        self.editU = wx.TextCtrl(panel, size=(140, -1))
        self.editC = wx.TextCtrl(panel, size=(140, -1))

        self.sizer = wx.GridBagSizer(5, 1)
        self.sizer.Add(self.lblAgle, (0, 0))
        self.sizer.Add(self.editAgle, (0, 1))
        self.sizer.Add(self.lblU, (1, 0))
        self.sizer.Add(self.editU, (1, 1))
        self.sizer.Add(self.lblС, (2, 0))
        self.sizer.Add(self.editC, (2, 1))
        self.sizer.Add(self.button, (3, 0), (0, 7), flag=wx.EXPAND)

        panel.SetSizer(self.sizer)

        # Set Binds
        self.button.Bind(wx.EVT_BUTTON, self.calculation)

        # Set values
        self.editAgle.SetValue("30")
        self.editU.SetValue("1")
        self.editC.SetValue("1")

        self.Show()

    def calculation(self, e):
        print("Angle = ", self.editAgle.GetValue())
        print("U = ", self.editU.GetValue())
        print("C = ", self.editC.GetValue())


if __name__ == '__main__':
    app = wx.App(False)
    frame = ShowApplication()
    app.MainLoop()