import os
import wx

class ViewScreenshot(wx.Frame):
    def __init__(self, parent, id = -1, title = 'Screenshot Viewer' ):
        wx.Frame.__init__(self, parent, id, title)
        self.panel = wx.Panel(self)
        self.photo_max_size = 240
        self.current_file = ""
        self.__create_gui()
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        
    def __create_gui(self):
        self.image = wx.EmptyImage(240,240)
        self.image_ctrl = wx.StaticBitmap(self.panel, wx.ID_ANY,
                                       wx.BitmapFromImage(self.image))


        self.main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.main_sizer.Add(self.image_ctrl, 0, wx.ALL|wx.EXPAND)


        self.panel.SetSizer(self.main_sizer)
        self.panel.Fit()
        self.panel.Layout()
        

    def ShowScrnshot(self, element):
        self.current_file = element.get("path")
        self.image = wx.Image(self.current_file, wx.BITMAP_TYPE_ANY)
        # scale the image, preserving the aspect ratio
        w = self.image.GetWidth()
        h = self.image.GetHeight()
        dsize = wx.GetDisplaySize()
        if w >= dsize.GetWidth() or h >= dsize.GetHeight():
            h = dsize.GetHeight() - dsize.GetHeight() / 3
            w = dsize.GetWidth() - dsize.GetWidth() / 3
            self.image = self.image.Scale(w,h)        


        self.image_ctrl.SetBitmap(wx.BitmapFromImage(self.image))
        self.panel.Refresh()
        self.SetSize((w,h))
        self.Center()
        self.Show()

    def GetImage(self):
        return self.image

    def OnClose(self, event):
        self.Hide()
        
