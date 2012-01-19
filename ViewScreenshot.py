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
  
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.main_sizer.Add(self.image_ctrl, 0, wx.ALL|wx.EXPAND)

        self.panel.SetSizer(self.main_sizer)
        self.panel.Fit()
        self.panel.Layout()
        

    def ShowScrnshot(self, element):
        filepath = element.get("path")
        self.image = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        # scale the image, preserving the aspect ratio
        w = self.image.GetWidth()
        h = self.image.GetHeight()
        if w > h:
            new_w = self.photo_max_size
            new_h = self.photo_max_size * h / w
        else:
            new_h = self.photo_max_size
            new_w = self.photo_max_size * w / h
            self.image = self.image.Scale(new_w,new_h)

        self.image_ctrl.SetBitmap(wx.BitmapFromImage(self.image))
        self.current_file = element.get("path")
        self.panel.Refresh()
        self.SetSize((w, h))
        self.Show()

    def GetImage(self):
        return self.image

    def OnClose(self, event):
        self.Hide()
        
