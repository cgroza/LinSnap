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
# from Threads import *

class ThumbnailView(ThumbnailCtrl):
    """
    This class manages the thumbnail display and related events and functions.
    """
    def __init__(self, parent, app_instance, id):
        self.parent = parent
        self.app_instance = app_instance
        self.collections = self.app_instance.collections
        self.collection_list = self.app_instance.collection_list
        # Note: Using PIL causes the program to freeze.
        ThumbnailCtrl.__init__(self, self.parent, id, (-1, -1), (-1, -1),
                                   THUMB_OUTLINE_RECT, THUMB_FILTER_IMAGES)

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

        self.Bind(wx.EVT_MENU, self.OnViewScrnshot, id = 1000)
        self.Bind(wx.EVT_MENU, self.OnMenuRename, id = 1005)
        self.Bind(wx.EVT_MENU, self.OnMenuDelete, id = 1010)
        self.Bind(wx.EVT_MENU, self.OnMenuMove, id = 1015)
        self.Bind(wx.EVT_MENU, self.OnMenuUpload, id = 1020)
        self.Bind(wx.EVT_MENU, self.OnMenuEditTags, id = 1025)
        self.scroll_ctrl.SetPopupMenu(self.popup_menu)


    def ShowCollection(self, collection):
        # thread = GenericThread(self.scroll_ctrl.ShowDir, collection.dir)
        # thread.start()
        self.app_instance.Freeze()
        self.scroll_ctrl.ShowDir(collection.dir)
	self.Thaw()

    def OnThumbClick(self, event):
        event.Skip()


    def OnThumbDoubleClick(self, event):
        event.Skip()

    def OnMenuUpload(self, event):
        thumb = self.GetSelectedThumbnail()
        if thumb is not None:
            self.app_instance.upload_win.SetUploadFiles([thumb.GetOriginalImage()])
        
        self.app_instance.upload_win.upload_choice.SetSelection(0)
        self.app_instance.upload_win.Show()
        event.Skip()

    def OnMenuRename(self, event):
        self.RenameScreenshot()
        event.Skip()

    def RenameSelectedCollection(self):
        col_name = self.app_instance.GetSelectedCollection()
        dlg = wx.TextEntryDialog(None, "Rename collection to: ", "Rename Collection")
        resp = dlg.ShowModal()
        if resp == wx.ID_OK:
            new_col_name = dlg.GetValue()
            if new_col_name and new_col_name not in self.app_instance.collections.collections:
                self.collections.RenameCollection(col_name, new_col_name)
                self.collection_list.SetItemText(self.app_instance.collection_list.GetFocusedItem(), new_col_name)
            else:
                wx.MessageDialog(None, "Invalid collection name. Name already exists or empty.", "Name Error", wx.ICON_EXCLAMATION).ShowModal()


    def OnMenuDelete(self, event):
        self.DeleteScreenshot()
        event.Skip()

    def OnMenuMove(self, event):
        self.MoveScreenshot()
        event.Skip()

    def OnMenuEditTags(self, event):
        self.EditTags()
        event.Skip()

    def EditTags(self):
        thumb = self.GetSelectedThumbnail()
        if thumb is not None:
            elem = self.app_instance.collections.FindElement(thumb.GetOriginalImage())
            if elem is not None: 
                self.app_instance.edit_tags_win.SetTargetElement(elem)
                self.app_instance.edit_tags_win.Show()

    def _GetCurrentCollection(self):
        collection_name = self.app_instance.collection_list.GetItemText(self.app_instance.collection_list.GetFocusedItem())
        return self.app_instance.collections.GetCollection(collection_name)

    def GetSelectedScrnName(self):
        index = self.scroll_ctrl.GetSelection()
        if index > -1:
            return self.scroll_ctrl.GetItem(index).GetFileName()

    def DeleteScreenshot(self):
        thumb_index = self.scroll_ctrl.GetSelection()
        dlg = wx.MessageDialog(None, "Are you sure? The real file will be deleted!", "Delete Screenshot", style = wx.ICON_QUESTION | wx.YES_NO)
        resp = dlg.ShowModal()
        if resp == wx.ID_YES and thumb_index != -1:
            thumb = self.scroll_ctrl.GetItem(thumb_index)
            self.app_instance.collections.FindFileAndDelete(thumb.GetOriginalImage())
            self.scroll_ctrl.RemoveItemAt(thumb_index)

    def MoveScreenshot(self):
        thumb = self.GetSelectedThumbnail()
        if thumb is not None:
            # get destination collection
            dlg = MoveScrnDlg(self, -1, self.app_instance.collections.collections.keys())
            data = dlg.ShowModal()
            dest_collection_name = data[1]
            if dest_collection_name and data[0] == wx.ID_OK:
                element = self.app_instance.collections.FindElement(thumb.GetOriginalImage())
                dest_collection = self.app_instance.collections.GetCollection(dest_collection_name)
                if element is not None and dest_collection:
                    thumb_index = self.scroll_ctrl.GetSelection()
                    self.app_instance.collections.FindAndRemoveElement(element.get("path"))
                    self.app_instance.collections.MoveElement(element, dest_collection)
                    self.scroll_ctrl.RemoveItemAt(thumb_index)


    def RenameScreenshot(self):
        dlg = wx.TextEntryDialog(None, "Rename screenshot to: ", "Rename Screenshot")
        resp = dlg.ShowModal()
        if resp == wx.ID_OK:
            new_scrn_name = dlg.GetValue()
            thumb = self.GetSelectedThumbnail()
            if thumb is not None:
                element = self.app_instance.collections.FindElement(thumb.GetOriginalImage())
                if new_scrn_name and element is not None:
                    element_name = element.get("name")
                    new_scrn_name += "." + element_name.split(".")[-1]
                    self.app_instance.collections.FindParentCollection(element).RenameElement(
                        element_name, new_scrn_name)
                    thumb.SetCaption(new_scrn_name)
                    thumb.SetFileName(new_scrn_name)
                    self.scroll_ctrl.UpdateProp()
                else:
                    wx.MessageDialog(None, "Invalid screenshot name. Name already exists or empty.", "Name Error", wx.ICON_EXCLAMATION).ShowModal()


    def OnViewScrnshot(self, event):
        self.ViewScreenshot()
        event.Skip()


    def ViewScreenshot(self):
        thumb_index = self.scroll_ctrl.GetSelection()
        if thumb_index != -1:
            thumb = self.scroll_ctrl.GetItem(thumb_index)
            element = self.app_instance.collections.FindElement(thumb.GetOriginalImage())
            if element is not None:
                self.app_instance.scrn_viewer.ShowScrnshot(element)

        

    def ShowFiles(self, file_list):
        thumbs = []
        # build thumbnail objects for every file
        for path in file_list:
            directory, filename = os.path.split(path)
            thumbs.append(Thumb(self.scroll_ctrl, directory, filename, filename))
        max_index = self.GetItemCount() - 1
        self.Freeze()
        self.scroll_ctrl.Clear()
        self.scroll_ctrl.ShowThumbs(thumbs, "Search Result")
        self.Thaw()

    def GetSelectedThumbnail(self):
        thumb_index = self.scroll_ctrl.GetSelection()
        if thumb_index != -1:
            return self.scroll_ctrl.GetItem(thumb_index)
