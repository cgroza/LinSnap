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

import wx

class LinSnap(wx.Frame):
    """
    This is the main program class. It will assemble the GUI and hold generic functions.
    """
    def __init__(self, id, parent):
        self.parent = parent
        self.id = id
        wx.Frame.__init__(self, self.parent, id)
    

def main():
    lin_snap_app = wx.PySimpleApp()
    lin_snap_frame = LinSnap( -1, None )
    lin_snap_frame.Show()
    lin_snap_app.MainLoop()


if __name__ == "__main__":
    main()
