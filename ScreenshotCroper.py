import wx
import wx.lib.mixins.rubberband as rubberband
from ViewScreenshot import *


class ScreenshotCroper(ViewScreenshot):
    def __init__(self, parent, id = -1):
        ViewScreenshot.__init__(self, parent, id)

        # Create the rubberband
        self.rubber_band = rubberband.RubberBand(drawingSurface = self.image_ctrl)
        self.rubber_band.reset(aspectRatio=0.5)
        self.crop_btn = wx.Button(self.panel, -1, "Crop")
        self.save_btn = wx.Button(self.panel, -1, "Save")

        self.crop_btn.Bind(wx.EVT_BUTTON, self.OnCrop)
        self.main_sizer.Add(self.crop_btn, 0, wx.ALL|wx.EXPAND)
        self.main_sizer.Add(self.save_btn, 0, wx.ALL|wx.EXPAND)
        self.panel.Fit()
        self.Fit()

    def CropImage(self):
        coords = self.rubber_band.getCurrentExtent()

        if coords is None:
            return

        x0, y0, x1, y1 = coords
        width = x1 - x0
        height = y1 - y0

        self.image = self.image.GetSubImage(wx.Rect(x0, y0, width, height))

        self.image_ctrl.SetBitmap(wx.BitmapFromImage(self.image))
        self.image.SaveFile(self.current_file, wx.BITMAP_TYPE_PNG)
        self.rubber_band.reset()

    def OnCrop(self, event):
        self.CropImage()
        event.Skip()

    def ShowScrnshot(self, element):
        ViewScreenshot.ShowScrnshot(self, element)
        sz = self.GetSize()
        self.SetSize((sz.GetWidth(), sz.GetHeight() + 60))
        self.rubber_band.reset()
