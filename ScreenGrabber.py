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

class ScreenGrabberWindow(wx.Frame):
    """
    This class impelements a window that will collect a the necessary information.
    """

    def __init__(self, *args, **kwds):
        # begin wxGlade: SreenGrabberWindow.__init__
        
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.top_panel = wx.Panel(self, -1)
        self.save_label = wx.StaticText(self.top_panel, -1, "Pick a colection to save the screenshot in:")
        self.choice_collection = wx.Choice(self.top_panel, -1, choices=[])
        self.scrn_opt_label = wx.StaticText(self.top_panel, -1, "Screenshot options:")
        self.options_radio_box = wx.RadioBox(self.top_panel, -1, "Capture", choices=["Whole screen", "Current window", "Selected region"], majorDimension=0, style=wx.RA_SPECIFY_COLS)
        self.delay_label = wx.StaticText(self.top_panel, -1, "Screenshot delay: ")
        self.delay_spin_ctrl = wx.SpinCtrl(self.top_panel, -1, "1", min=0, max=100, style=wx.SP_ARROW_KEYS|wx.SP_WRAP|wx.TE_AUTO_URL|wx.TE_NOHIDESEL)
        self.bt_take_scrn = wx.Button(self.top_panel, -1, "Take Screenshot")
        self.bt_cancel = wx.Button(self.top_panel, -1, "Cancel")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: SreenGrabberWindow.__set_properties
        self.SetTitle("frame_1")
        self.SetSize((577, 302))
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
        v_top_sizer.Add(self.save_label, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0)
        v_top_sizer.Add(self.choice_collection, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 0)
        v_sizer.Add(v_top_sizer, 0, wx.EXPAND, 0)
        scrn_opt_v_sizer.Add(self.scrn_opt_label, 0, wx.ALL|wx.EXPAND, 0)
        scrn_opt_v_sizer.Add(self.options_radio_box, 0, wx.ALL|wx.EXPAND, 0)
        delay_h_sizer.Add(self.delay_label, 0, wx.ALL|wx.EXPAND, 0)
        delay_h_sizer.Add(self.delay_spin_ctrl, 0, wx.LEFT|wx.RIGHT, 0)
        scrn_opt_v_sizer.Add(delay_h_sizer, 0, wx.ALL|wx.EXPAND, 3)
        v_sizer.Add(scrn_opt_v_sizer, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 0)
        h_bt_sizer.Add(self.bt_take_scrn, 0, wx.RIGHT|wx.BOTTOM|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 0)
        h_bt_sizer.Add(self.bt_cancel, 0, wx.RIGHT|wx.BOTTOM|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 0)
        v_sizer.Add(h_bt_sizer, 0, wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT|wx.SHAPED, 1)
        self.top_panel.SetSizer(v_sizer)
        top_sizer.Add(self.top_panel, 1, wx.EXPAND, 0)
        self.SetSizer(top_sizer)
        self.Layout()
        # end wxGlade

    def OnTakeScreenshot(self, event):
        pass

    def OnClose(self, event):
        pass
    # end of class SreenGrabberWindow

class ScreenGrabber():
    """
    This class manages the screenshot taking process.
    """
    def __init__(self):
        pass


    def TakeScreenshot(self):
        pass


