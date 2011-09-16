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

import wx
import CollectionManager
import CollectionDatabase
# begin wxGlade: extracode
# end wxGlade



class SreenGrabberWindow(wx.Frame):
    def __init__(self, collection_db, parent, id = -1):
        # begin wxGlade: SreenGrabberWindow.__init__
        wx.Frame.__init__(self, parent , id, style = wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX |
                          wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)

        self.collection_db = collection_db
        self.top_panel = wx.Panel(self, -1)
        self.save_label = wx.StaticText(self.top_panel, -1, "Pick a colection to save the screenshot in:")
        self.choice_collection = wx.Choice(self.top_panel, -1, choices= collection_db.collections.keys())
        self.filename_label = wx.StaticText(self.top_panel, -1, "Screenshot file name:")
        self.filename_text = wx.TextCtrl(self.top_panel, -1, "")
        self.scrn_opt_label = wx.StaticText(self.top_panel, -1, "Screenshot options:")
        self.options_radio_box = wx.RadioBox(self.top_panel, -1, "Capture", choices=["Whole screen", "Current window", "Selected region"], majorDimension=0, style=wx.RA_SPECIFY_COLS)
        self.delay_label = wx.StaticText(self.top_panel, -1, "Screenshot delay: ")
        self.delay_spin_ctrl = wx.SpinCtrl(self.top_panel, -1, "1", min=0, max=100, style=wx.SP_ARROW_KEYS|wx.SP_WRAP|wx.TE_AUTO_URL|wx.TE_NOHIDESEL)
        self.bt_take_scrn = wx.Button(self.top_panel, -1, "Take Screenshot")
        self.bt_cancel = wx.Button(self.top_panel, -1, "Cancel")

        self.__selecting_region = False
        self.__take_screenshot = False
        self.__start_mouse_pos = (0,0)
        self.__end_mouse_pos = (0,0)

        self.__set_properties()
        self.__do_layout()
        self.__bind_events()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: SreenGrabberWindow.__set_properties
        self.SetTitle("Take Screenshot")
        self.SetSize((400, 200))
        self.options_radio_box.SetSelection(0)
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
        scrn_opt_v_sizer.Add(self.scrn_opt_label, 0, wx.ALL|wx.EXPAND, 0)
        scrn_opt_v_sizer.Add(self.options_radio_box, 0, wx.ALL|wx.EXPAND, 0)
        delay_h_sizer.Add(self.delay_label, 0, wx.ALL|wx.EXPAND, 0)
        delay_h_sizer.Add(self.delay_spin_ctrl, 0, wx.LEFT|wx.RIGHT, 0)
        scrn_opt_v_sizer.Add(delay_h_sizer, 0, wx.ALL|wx.EXPAND, 3)
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
        self.top_panel.Bind(wx.EVT_LEFT_UP, self.OnMouseLeftUp)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftDown)
        self.Bind(wx.EVT_MOTION, self.OnMouseMove)

    def SetCollectionList(self, collections):
        self.choice_collection.SetItems(collections)

    def OnTakeScreenshot(self, event):
        print "OnTakeScreenshot"
        self.__take_screenshot = True
        event.Skip()

    def OnMouseLeftDown(self, event):
        print "OnMouseLeftDown"
        if self.__take_screenshot:
            self.__start_mouse_pos = event.GetPosTuple()

        event.Skip()

    def OnMouseLeftUp(self, event):
        print "OnMouseLeftUp"
        if self.__take_screenshot:
            self.__selecting_region = False
            self.__end_mouse_pos = event.GetPosTuple()
            self.TakeScreenshot()

        event.Skip()

    def OnMouseMove(self, event):
        print "OnMouseMove"
        if self.__take_screenshot and self.__selecting_region and event.Dragging():
            pass
        event.Skip()

    def TakeScreenshot(self):
        collection_name = self.choice_collection.GetStringSelection()
        scrn_filename = self.filename_text.GetValue()
        scrn_rect = (self.__start_mouse_pos, self.__end_mouse_pos)

        if not collection_name:
            wx.MessageDialog(None, "No collection selected. Please choose a collection.", "Error", wx.OK | wx.ICON_ERROR).ShowModal()
            return

        selected_col = self.collection_db.GetCollection(collection_name)
        if not scrn_filename or not selected_col.FindElement(scrn_filename):
            wx.MessageDialog(None, "Invalid file name. File name is empty or already exists.", "Error", wx.OK | wx.ICON_ERROR).ShowModal()
            return

        scrn_shot_bmp = ScreenGrabber.TakeScreenShot(scrn_rect)
        self.__take_screenshot = False
        scrn_img = scrn_shot_bmp.ToImage()
        path = os.path.join(selected_col.dir, scrn_filename)
        scrn_img.Save(path)
        elem_attrs = { "tags" : "", "name" : scrn_filename, "path" : path }
        selected_col.CreateElement(elem_attrs)
        self.parent.thumbnail_view.scroll_ctrl.UpdateShow()

    def OnClose(self, event):
        self.filename_text.Clear()
        self.Hide()
    # end of class SreenGrabberWindow

class ScreenGrabber():
    """
    This class manages the screenshot taking process.
    """

    @staticmethod
    def TakeScreenShot(self, rect):
        """ Takes a screenshot of the screen at give pos & size (rect). """

        #Create a DC for the whole screen area
        dcScreen = wx.ScreenDC()

        #Create a Bitmap that will later on hold the screenshot image
        #Note that the Bitmap must have a size big enough to hold the screenshot
        #-1 means using the current default colour depth
        bmp = wx.EmptyBitmap(rect.width, rect.height)

        #Create a memory DC that will be used for actually taking the screenshot
        memDC = wx.MemoryDC()

        #Tell the memory DC to use our Bitmap
        #all drawing action on the memory DC will go to the Bitmap now
        memDC.SelectObject(bmp)

        #Blit (in this case copy) the actual screen on the memory DC
        #and thus the Bitmap
        memDC.Blit( 0, #Copy to this X coordinate
            0, #Copy to this Y coordinate
            rect.width, #Copy this width
            rect.height, #Copy this height
            dcScreen, #From where do we copy?
            rect.x, #What's the X offset in the original DC?
            rect.y  #What's the Y offset in the original DC?
            )

        #Select the Bitmap out of the memory DC by selecting a new
        #uninitialized Bitmap
        memDC.SelectObject(wx.NullBitmap)

        return bmp 

if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    scrn_grabber_win = SreenGrabberWindow(None, None, -1)
    app.SetTopWindow(scrn_grabber_win)
    scrn_grabber_win.Show()
    app.MainLoop()
