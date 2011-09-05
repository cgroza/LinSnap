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

class ThumbnailView(ThumbnailCtrl):
    """
    This class manages the thumbnail display and related events and functions.
    """
    def __init__(self, parent, id = -1):
        self.parent = parent
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

        self.scroll_ctrl.SetPopupMenu(self.popup_menu)

    def OnThumbClick(self, event):
        pass


    def OnThumbDoubleClick(self, event):
        pass
