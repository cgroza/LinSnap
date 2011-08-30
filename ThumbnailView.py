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
        

    def OnThumbClick(self, event):
        pass


    def OnThumbDoubleClick(self, event):
        pass
