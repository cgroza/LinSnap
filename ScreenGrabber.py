#  Copyright (C) 2011  Groza Cristian
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx, os
import CollectionManager
import CollectionDatabase
from ScreenshotCroper import *

class ScreenGrabber():
    """
    This class manages the screenshot taking process.
    """


    @staticmethod
    def TakeScreenshot(save_path):
        """ Takes a screenshot of the screen at give pos & size (rect). """
        #Create a DC for the whole screen area
        dcScreen = wx.ScreenDC()

        #Create a Bitmap that will later on hold the screenshot image
        #Note that the Bitmap must have a size big enough to hold the screenshot
        #-1 means using the current default colour depth
        rect = wx.GetDisplaySize()

        bmp = wx.EmptyBitmap(rect.GetWidth(), rect.GetHeight())
        #Create a memory DC that will be used for actually taking the screenshot
        memDC = wx.MemoryDC()
        #Tell the memory DC to use our Bitmap
        #all drawing action on the memory DC will go to the Bitmap now
        memDC.SelectObject(bmp)
        #Blit (in this case copy) the actual screen on the memory DC
        #and thus the Bitmap
        memDC.Blit( 0, #Copy to this X coordinate
            0, #Copy to this Y coordinate
            rect.GetWidth(), #Copy this width
            rect.GetHeight(), #Copy this height
            dcScreen, #From where do we copy?
            0, #What's the X offset in the original DC?
            0)  #What's the Y offset in the original DC?
        #Select the Bitmap out of the memory DC by selecting a new
        #uninitialized Bitmap
        memDC.SelectObject(wx.NullBitmap)
        # save screenshot in the collection folder
        bmp.ConvertToImage().SaveFile(save_path, wx.BITMAP_TYPE_PNG)
        


class ScreenGrabberWindow(wx.Frame):
    class ScrnShotTimer(wx.Timer):
        def __init__(self, func):
            wx.Timer.__init__(self)
            self.__func = func

        def Notify(self):
            self.__func()

    def __init__(self, collection_db, parent, id = -1):
        # begin wxGlade: SreenGrabberWindow.__init__
        wx.Frame.__init__(self, parent , id, style = wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX |
                          wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)

        self.crop_win = ScreenshotCroper(self)
        self.parent = parent
        self.collection_db = collection_db
        self.top_panel = wx.Panel(self, -1)
        self.save_label = wx.StaticText(self.top_panel, -1, "Pick a colection to save the screenshot in:")
        self.choice_collection = wx.Choice(self.top_panel, -1, choices= collection_db.collections.keys())
        self.filename_label = wx.StaticText(self.top_panel, -1, "Screenshot file name:")
        self.filename_text = wx.TextCtrl(self.top_panel, -1, "")

        self.delay_label = wx.StaticText(self.top_panel, -1, "Screenshot delay: ")
        self.delay_spin_ctrl = wx.SpinCtrl(self.top_panel, -1, "1", min=0, max=100, style=wx.SP_ARROW_KEYS|wx.SP_WRAP|wx.TE_AUTO_URL|wx.TE_NOHIDESEL)
        self.hide_linsnap = wx.CheckBox(self.top_panel, -1, "Hide LinSnap")
        self.bt_take_scrn = wx.Button(self.top_panel, -1, "Take Screenshot")
        self.bt_cancel = wx.Button(self.top_panel, -1, "Cancel")


        self.__take_screenshot = False

        self.__set_properties()
        self.__do_layout()
        self.__bind_events()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: SreenGrabberWindow.__set_properties
        self.SetTitle("Take Screenshot")
        self.SetSize((400, 170))
        self.bt_take_scrn.SetFocus()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: SreenGrabberWindow.__do_layout
        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        v_sizer = wx.BoxSizer(wx.VERTICAL)
        h_bt_sizer = wx.BoxSizer(wx.HORIZONTAL)
        scrn_opt_v_sizer = wx.BoxSizer(wx.VERTICAL)
        delay_h_sizer = wx.BoxSizer(wx.HORIZONTAL)
        v_top_sizer = wx.BoxSizer(wx.VERTICAL)
        h_filename_sizer = wx.BoxSizer(wx.HORIZONTAL)
        filename_txt_sz = wx.BoxSizer(wx.VERTICAL)
        v_top_sizer.Add(self.save_label, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0)
        v_top_sizer.Add(self.choice_collection, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 0)
        h_filename_sizer.Add(self.filename_label, 0, wx.ALL|wx.EXPAND, 0)
        filename_txt_sz.Add(self.filename_text, 0, wx.ALL|wx.EXPAND, 0)
        h_filename_sizer.Add(filename_txt_sz, 1, wx.EXPAND, 0)
        v_top_sizer.Add(h_filename_sizer, 1, wx.EXPAND, 0)
        v_sizer.Add(v_top_sizer, 0, wx.EXPAND, 0)
        delay_h_sizer.Add(self.delay_label, 0, wx.ALL|wx.EXPAND, 0)
        delay_h_sizer.Add(self.delay_spin_ctrl, 0, wx.LEFT|wx.RIGHT, 0)
        scrn_opt_v_sizer.Add(delay_h_sizer, 0, wx.ALL|wx.EXPAND, 3)
        scrn_opt_v_sizer.Add(self.hide_linsnap, 0, wx.ALL|wx.EXPAND, 0)
        v_sizer.Add(scrn_opt_v_sizer, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 0)
        h_bt_sizer.Add(self.bt_take_scrn, 0, wx.RIGHT|wx.BOTTOM|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 0)
        h_bt_sizer.AddSpacer(5)
        h_bt_sizer.Add(self.bt_cancel, 0, wx.RIGHT|wx.BOTTOM|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 0)
        v_sizer.Add(h_bt_sizer, 0, wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT|wx.SHAPED)
        self.top_panel.SetSizer(v_sizer)
        top_sizer.Add(self.top_panel, 1, wx.EXPAND, 0)
        self.SetSizer(top_sizer)
        self.Layout()
        # end wxGlade

    def __bind_events(self):
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.bt_take_scrn.Bind(wx.EVT_BUTTON, self.OnTakeScreenshot)
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnClose)


    def SetCollectionList(self, collections):
        self.choice_collection.SetItems(collections)

    def SetCurrentCollection(self, collection_name):
        self.choice_collection.SetStringSelection(collection_name)

    def OnTakeScreenshot(self, event):
        self.__take_screenshot = True
        # Hide LinSnap
        if self.hide_linsnap.GetValue():
            self.parent.Hide()
            # Hide screenshot whindow
        self.Hide()
        # shoot right away if delay is 0
        if self.delay_spin_ctrl.GetValue() == 0:
            self.TakeScreenshot()
        # else, create a timer
        else:
            self.timer = self.__class__.ScrnShotTimer(self.TakeScreenshot)
            self.timer.Start( 1000 * self.delay_spin_ctrl.GetValue(), True)

        event.Skip()

    def TakeScreenshot(self):
        collection_name = self.choice_collection.GetStringSelection()
        scrn_filename = self.filename_text.GetValue()

        if not collection_name:
            wx.MessageDialog(None, "No collection selected. Please choose a collection.", "Error", wx.OK | wx.ICON_ERROR).ShowModal()
            return

        selected_col = self.collection_db.GetCollection(collection_name)
        if not scrn_filename or selected_col.FindElement(scrn_filename):
            wx.MessageDialog(None, "Invalid file name. File name is empty or already exists.", "Error", wx.OK | wx.ICON_ERROR).ShowModal()
            return

        # we may have to move all this in a separate thread because it hangs the UI.
        path = os.path.join(selected_col.dir, scrn_filename) + ".png"
        # get current selected screenshot option and call the appropriate procedure via the dict.
        ScreenGrabber.TakeScreenshot(path)

        self.__take_screenshot = False

        # add it to the collection xml tree
        elem_attrs = { "tags" : "", "name" : scrn_filename, "path" : path }
        new_elem = selected_col.CreateElement(elem_attrs)
        # refresh the view
        self.parent.thumbnail_view.ShowCollection(self.parent.collections.GetCollection(collection_name))

        # bring back LinSnap windows
        self.parent.Show()
        self.Show()
        self.crop_win.ShowScrnshot(new_elem)

    def OnClose(self, event):
        # reset filename 
        self.filename_text.Clear()
        self.Hide()
    # end of class SreenGrabberWindow


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    scrn_grabber_win = SreenGrabberWindow(None, None, -1)
    app.SetTopWindow(scrn_grabber_win)
    scrn_grabber_win.Show()
    app.MainLoop()
