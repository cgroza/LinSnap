import wx
import wx.lib.mixins.rubberband as rubberband
from ViewScreenshot import *


class ScreenshotCroper(ViewScreenshot):
    def __init__(self, parent, id = -1):
        ViewScreenshot.__init__(self, parent, id)
        self.menubar = wx.MenuBar( ) 
        self.scrnshot = wx.Menu()
        self.scrnshot.Append(1000, "Crop")
        self.scrnshot.Append(1010, "Save")
        self.scrnshot.Append(1020, "Reset")
        self.scrnshot.Append(1030, "Close")
        self.menubar.Append(self.scrnshot, "Screenshot")
        self.SetMenuBar(self.menubar)

        self.Bind(wx.EVT_MENU, self.OnCrop, id = 1000)
        self.Bind(wx.EVT_MENU, self.OnSave , id = 1010)
        self.Bind(wx.EVT_MENU, self.OnReset , id = 1020)
        self.Bind(wx.EVT_MENU, self.OnClose , id = 1030)

        # Create the rubberband
        self.rubber_band = rubberband.RubberBand(drawingSurface = self.image_ctrl)
        self.rubber_band.reset(aspectRatio=0.5)

    def OnSave(self, event):
        self.image.SaveFile(self.current_element.get("path"), wx.BITMAP_TYPE_PNG)
        event.Skip()
        
    def OnReset(self, event):
        self.ShowScrnshot(self.current_element)
        event.Skip()
        
    def CropImage(self):
        coords = self.rubber_band.getCurrentExtent()
        if coords is None:
            return

        x0, y0, x1, y1 = coords
        width = x1 - x0
        height = y1 - y0

        self.image = self.image.GetSubImage(wx.Rect(x0, y0, width, height))
        self.image_ctrl.SetBitmap(wx.BitmapFromImage(self.image))
        self.rubber_band.reset()

    def OnCrop(self, event):
        self.CropImage()
        event.Skip()

    def ShowScrnshot(self, element):
        ViewScreenshot.ShowScrnshot(self, element)
        sz = self.GetSize()
        self.rubber_band.reset()
