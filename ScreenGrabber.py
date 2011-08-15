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

    def __init__(self, parent, id):
        self.parent = parent
        wx.Frame.__init__(self, self.parent, id)


    def OnTakeScreenshot(self, event):
        pass

    def OnClose(self, event):
        pass


class ScreenGrabber():
    """
    This class manages the screenshot taking process.
    """
    def __init__(self):
        pass


    def TakeScreenshot(self):
        pass


