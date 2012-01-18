import os
import wx

class ViewScreenshot(wx.Frame):
    def __init__(self, parent, id = -1):
        wx.Frame.__init__(self, parent, id, title='Screenshot Viewer')
        self.panel = wx.Panel(self)
        self.photo_max_size = 240
        self.__create_gui()
        
    def __create_gui(self):
        img = wx.EmptyImage(240,240)
        self.image_ctrl = wx.StaticBitmap(self.panel, wx.ID_ANY,
                                       wx.BitmapFromImage(img))
  
        self.main_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.main_sizer.Add(self.image_ctrl, 0, wx.ALL|wx.EXPAND)

        self.panel.SetSizer(self.main_sizer)
        self.panel.Fit()
        self.panel.Layout()
        

    def ShowScrnshot(self, element):
        filepath = element.get("path")
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        # scale the image, preserving the aspect ratio
        w = img.GetWidth()
        h = img.GetHeight()
        if w > h:
            new_w = self.photo_max_size
            new_h = self.photo_max_size * h / w
        else:
            new_h = self.photo_max_size
            new_w = self.photo_max_size * w / h
            img = img.Scale(new_w,new_h)

        self.image_ctrl.SetBitmap(wx.BitmapFromImage(img))
        self.panel.Refresh()
        self.SetSize((w, h))
        self.Show()

    def OnClose(event):
        self.Hide()
        
