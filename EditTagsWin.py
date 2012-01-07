#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Sat Jan  7 11:54:58 2012

import wx

# begin wxGlade: extracode
# end wxGlade



class EditTagsWin(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: EditTagsWin.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.tags_info = wx.StaticText(self, -1, " Current tags of item:")
        self.tags_txt_ctrl = wx.TextCtrl(self, -1, "")
        self.ok_bt = wx.Button(self, -1, "OK")
        self.cancel_bt = wx.Button(self, -1, "Cancel")

        self.__set_properties()
        self.__bind_events()
        self.__do_layout()

        # end wxGlade

        self.target_elem = None

    def __set_properties(self):
        # begin wxGlade: EditTagsWin.__set_properties
        self.SetTitle("Edit Sceenshot Tags")
        self.SetSize((334, 98))
        self.SetFocus()
        # end wxGlade

    def __bind_events(self):
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.ok_bt.Bind(wx.EVT_BUTTON, self.OnButtonOk)
        self.cancel_bt.Bind(wx.EVT_BUTTON, self.OnClose)

    def __do_layout(self):
        # begin wxGlade: EditTagsWin.__do_layout
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        tags_sizer = wx.BoxSizer(wx.VERTICAL)
        ok_cancel_sizer = wx.BoxSizer(wx.HORIZONTAL)
        tags_sizer.Add(self.tags_info, 0, 0, 0)
        tags_sizer.Add((0, 15), 0, 0, 0)
        tags_sizer.Add(self.tags_txt_ctrl, 0, wx.ALL|wx.EXPAND, 0)
        ok_cancel_sizer.Add(self.cancel_bt, 0, 0, 0)
        ok_cancel_sizer.Add(self.ok_bt, 0, 0, 0)
        tags_sizer.Add(ok_cancel_sizer, 0, wx.ALIGN_RIGHT, 0)
        main_sizer.Add(tags_sizer, 1, wx.EXPAND, 0)
        self.SetSizer(main_sizer)
        self.Layout()
        # end wxGlade

    def OnClose(self, event):
        self.Hide()

    def OnButtonOk(self, event):
        self.target_elem.set("tags", " ".join(map(unicode.strip, self.tags_txt_ctrl.GetValue().split(","))))
        self.GetParent().collections.FindParentCollection(self.target_elem).SaveTree()
        self.Hide()

    def SetTargetElement(self, element):
        self.target_elem = element
        self.tags_txt_ctrl.SetValue(",".join(element.get("tags").split()))

# end of class EditTagsWin


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    edit_tags_win = EditTagsWin(None, -1, "")
    app.SetTopWindow(edit_tags_win)
    edit_tags_win.Show()
    app.MainLoop()
