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
from wx.lib.agw.thumbnailctrl import *
from MoveScrnDlg import *

class ThumbnailView(ThumbnailCtrl):
    """
    This class manages the thumbnail display and related events and functions.
    """
    def __init__(self, parent, app_instance, id):
        self.parent = parent
        self.app_instance = app_instance
        ThumbnailCtrl.__init__(self, self.parent, id, (-1, -1), (-1, -1),
                                   THUMB_OUTLINE_RECT, THUMB_FILTER_IMAGES, PILImageHandler)

        self.scroll_ctrl = self._scrolled
        # Creote popup menu, this menu will appear when the user will click on a thumbnail
        self.popup_menu = wx.Menu()
        # Add popup menu elements
        self.popup_menu.Append(1000, "View", "Open a preview of the selected thumbnail.")
        self.popup_menu.Append(1005, "Rename", "Rename the selected thumbnail.")
        self.popup_menu.Append(1010, "Delete", "Delete the selected thumbnail. The real file is deleted also.")
        self.popup_menu.Append(1015, "Move", "Move the selected thumbnail to antother collection.")
        self.popup_menu.Append(1020, "Upload", "Upload the thumbnail to a web service.")
        self.popup_menu.Append(1025, "Edit Tags", "Edit the tags of the selected thumbnail.")

        self.Bind(wx.EVT_MENU, self.OnMenuUpload, id = 1020)

        self.scroll_ctrl.SetPopupMenu(self.popup_menu)



    def OnThumbClick(self, event):
        pass


    def OnThumbDoubleClick(self, event):
        pass


    def OnMenuUpload(self, event):
        file_path = os.path.join(self.GetShowDir(), self.scroll_ctrl.GetItem(self.scroll_ctrl.GetSelection()).GetFileName())
        # self.app_instance.upload_win.SetUploadFiles([file_path])
        self.app_instance.upload_win.SetSelection(0)
        self.app_instance.upload_win.Show()

    def OnMenuRename(self, event):
        item_name = self.scroll_ctrl.GetItem(self.scroll_ctrl.GetSelection()).GetFileName()

    def OnMenuDelete(self, event):
        item_name = self.scroll_ctrl.GetItem(self.scroll_ctrl.GetSelection()).GetFileName()

    def OnMenuMove(self, event):
        item_name =  self.scroll_ctrl.GetItem(self.scroll_ctrl.GetSelection()).GetFileName()

    def OnMenuEditTags(self, event):
        item_name = self.scroll_ctrl.GetItem(self.scroll_ctrl.GetSelection()).GetFileName()

    def _GetCurrentCollection(self):
        collection_name = self.app_instance.collection_list.GetItemText(self.app_instance.collection_list.GetFocusedItem())
        return self.app_instance.collections.GetCollection(collection_name)

    def GetSelectedScrnName(self):
        index = self.scroll_ctrl.GetSelection()
        if index > -1:
            return self.scroll_ctrl.GetItem(index).GetFileName()

    def DeleteScreenshot(self):
        scrn_name = self.GetSelectedScrnName()
        col_name = self.app_instance.GetSelectedCollection()
        if scrn_name and col_name:
            dlg = wx.MessageDialog(None, "Are you sure? The real file will be deleted!", "Delete Screenshot", style = wx.ICON_QUESTION)
            resp = dlg.ShowModal()
            if resp == wx.ID_OK:
                collection = self.app_instance.collections.GetCollection(col_name)
                if collection:
                    collection.DeleteElement(scrn_name)
                    self.scroll_ctrl.ShowDir(self.scroll_ctrl.GetShowDir())


    def MoveScreenshot(self):
        scrn_name = self.GetSelectedScrnName()
        col_name = self.app_instance.GetSelectedCollection()
        if scrn_name and col_name:
            # get destination collection
            dlg = MoveScrnDlg(self, -1, self.app_instance.collections.collections.keys())
            data = dlg.ShowModal()
            dest_collection_name = data[1]

            if dest_collection_name and data[0] == wx.ID_OK:
                collection = self.app_instance.collections.GetCollection(col_name)
                dest_collection = self.app_instance.collections.GetCollection(dest_collection_name)
                if collection and dest_collection:
                    collection.MoveElement(scrn_name, dest_collection)
                    self.scroll_ctrl.ShowDir(self.scroll_ctrl.GetShowDir())


    def RenameScreenshot(self):
        scrn_name = self.GetSelectedScrnName()
        col_name = self.app_instance.GetSelectedCollection()
        if scrn_name and col_name:
            dlg = wx.TextEntryDialog(None, "Rename screenshot to: ", "Rename Screenshot")
            resp = dlg.ShowModal()
            if resp == wx.ID_OK:
                new_scrn_name = dlg.GetValue()
                collection = self.app_instance.collections.GetCollection(col_name)
                if new_scrn_name and collection:
                    collection.RenameElement(scrn_name, new_scrn_name + "." + scrn_name.split(".")[-1])
                    self.scroll_ctrl.ShowDir(self.scroll_ctrl.GetShowDir())
                else:
                    wx.MessageDialog(None, "Invalid screenshot name. Name already exists or empty.", "Name Error", wx.ICON_EXCLAMATION).ShowModal()

