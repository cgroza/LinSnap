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
# generated by wxGlade 0.6.3 on Mon Aug 15 11:41:57 2011

import wx
import os
import wx.lib.agw.thumbnailctrl
import ScreenGrabber
from ThumbnailView import *
from CollectionDatabase import *
from AddCollectionWin import *

# begin wxGlade: extracode
# end wxGlade



class LinSnap(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: LinSnap.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)

        self.HOMEDIR = os.path.expanduser("~")
        self.CFG_DIR = os.path.join(self.HOMEDIR, ".LinSnap")
        self.CFG_DIR_FILE = os.path.join(self.CFG_DIR,"LinSnap.cfg")

        if not self._CfgFilesExist():
            self._CreateCfgFiles()

        self.collections = CollectionDatabase(self.CFG_DIR_FILE, self.CFG_DIR)

        self.v_splitter = wx.SplitterWindow(self, -1, style=wx.SP_3D|wx.SP_BORDER)
        self.v_splitter_pane_2 = wx.Panel(self.v_splitter, -1)
        self.v_splitter_pane_1 = wx.Panel(self.v_splitter, -1)
        
        self.add_collection_win = AddCollectionWin(self)

        # Menu Bar
        self.lin_snap_frame_menubar = wx.MenuBar()
        self.SetMenuBar(self.lin_snap_frame_menubar)
        # Menu Bar end
        self.lin_snap_frame_statusbar = self.CreateStatusBar(1, 0)
        
        # Tool Bar
        self.lin_snap_frame_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.lin_snap_frame_toolbar)
        # Tool Bar end
        self.collection_list = wx.ListCtrl(self.v_splitter_pane_1, -1, style=wx.LC_LIST|wx.SUNKEN_BORDER)
        self.add_collection_bt = wx.Button(self.v_splitter_pane_1, -1, "Add Collection")

        self.thumbnail_view = ThumbnailView(self.v_splitter_pane_2, -1)
        
        self.__set_properties()
        self.__do_event_bindings()
        self.__do_layout()
        # end wxGlade

    def __do_event_bindings(self):
        self.add_collection_bt.Bind(wx.EVT_BUTTON, self.OnAddCollectionBt)

    def __set_properties(self):
        # begin wxGlade: LinSnap.__set_properties
        self.SetTitle("LinSnap")
        self.SetSize((700, 497))
        self.lin_snap_frame_statusbar.SetStatusWidths([-1])
        # statusbar fields
        lin_snap_frame_statusbar_fields = ["Done"]
        for i in range(len(lin_snap_frame_statusbar_fields)):
            self.lin_snap_frame_statusbar.SetStatusText(lin_snap_frame_statusbar_fields[i], i)
        self.lin_snap_frame_toolbar.Realize()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: LinSnap.__do_layout
        top_sizer = wx.BoxSizer(wx.VERTICAL)
        right_sizer = wx.BoxSizer(wx.HORIZONTAL)
        left_sizer = wx.BoxSizer(wx.VERTICAL)
        left_sizer.Add(self.collection_list, 1, wx.EXPAND, 0)
        left_sizer.Add(self.add_collection_bt, 0, wx.EXPAND, 0)
        self.v_splitter_pane_1.SetSizer(left_sizer)
        right_sizer.Add(self.thumbnail_view, 1, wx.EXPAND, 0)
        self.v_splitter_pane_2.SetSizer(right_sizer)
        self.v_splitter.SplitVertically(self.v_splitter_pane_1, self.v_splitter_pane_2)
        top_sizer.Add(self.v_splitter, 1, wx.EXPAND, 0)
        self.SetSizer(top_sizer)
        self.Layout()
        self.Centre()
        # end wxGlade

    def _CfgFilesExist(self):
        if os.path.exists(os.path.join(self.CFG_DIR)):
            if os.path.exists(self.CFG_DIR_FILE):
                return True
        return False

    def _CreateCfgFiles(self):
        if not os.path.exists(self.CFG_DIR):
            os.mkdir(self.CFG_DIR)
            with open(self.CFG_DIR_FILE, "w") as cfg_file:
                cfg_file.write("")
        elif not os.path.exists(self.CFG_DIR_FILE):
            with open(self.CFG_DIR_FILE, "w") as cfg_file:
                cfg_file.write("")
            
    def OnAddCollectionBt(self, event):
        self.add_collection_win.Show()

# end of class LinSnap


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    lin_snap_frame = LinSnap(None, -1, "")
    app.SetTopWindow(lin_snap_frame)
    lin_snap_frame.Show()
    app.MainLoop()
