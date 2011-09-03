#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Wed Aug 17 12:17:02 2011

import wx, os

# begin wxGlade: extracode
# end wxGlade



class AddCollectionWin(wx.Frame):
    def __init__(self, parent, id = -1):
        # begin wxGlade: AddCollectionWin.__init__
        self.parent = parent
        wx.Frame.__init__(self, self.parent, id)
        self.top_panel = wx.Panel(self)
        self.collection_name_label = wx.StaticText(self.top_panel, -1, "New collection name: ")
        self.collection_txt = wx.TextCtrl(self.top_panel, -1, "")
        self.collection_dir_label = wx.StaticText(self.top_panel, -1, "Collection directory: ")
        self.collection_dir_picker = wx.DirPickerCtrl(self.top_panel, -1, os.path.expanduser("~"))
        self.cancel_bt = wx.Button(self.top_panel, -1, "Cancel")
        self.add_collection_bt = wx.Button(self.top_panel, -1, "Add Collection")

        self.__set_properties()
        self.__do_event_bindings()
        self.__do_layout()
        # end wxGlade

    def __do_event_bindings(self):
        self.add_collection_bt.Bind(wx.EVT_BUTTON, self.OnAddCollectionBt)
        self.cancel_bt.Bind(wx.EVT_BUTTON, self.OnClose)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def __set_properties(self):
        # begin wxGlade: AddCollectionWin.__set_properties
        self.SetTitle("Add Collection")
        self.SetSize((430, 130))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: AddCollectionWin.__do_layout
        top_sizer = wx.BoxSizer(wx.VERTICAL)
        v_sizer = wx.BoxSizer(wx.VERTICAL)
        bt_h_sizer = wx.BoxSizer(wx.HORIZONTAL)
        collection_dir_sz = wx.BoxSizer(wx.HORIZONTAL)
        filepicker_sz = wx.BoxSizer(wx.VERTICAL)
        collection_name_sz = wx.BoxSizer(wx.HORIZONTAL)
        collection_text_sz = wx.BoxSizer(wx.VERTICAL)
        v_sizer.Add((20, 10), 0, 0, 0)
        collection_name_sz.Add(self.collection_name_label, 0, wx.ALL|wx.EXPAND, 0)
        collection_text_sz.Add(self.collection_txt, 1, wx.ALL|wx.EXPAND, 0)
        collection_name_sz.Add(collection_text_sz, 1, wx.ALL|wx.EXPAND, 0)
        v_sizer.Add(collection_name_sz, 0, wx.ALL|wx.EXPAND, 2)
        collection_dir_sz.Add(self.collection_dir_label, 1, wx.ALL|wx.EXPAND, 0)
        filepicker_sz.Add(self.collection_dir_picker, 2, wx.ALL|wx.EXPAND, 0)
        collection_dir_sz.Add(filepicker_sz, 0, wx.ALL|wx.EXPAND, 0)
        v_sizer.Add(collection_dir_sz, 0, wx.ALL|wx.EXPAND, 0)
        v_sizer.Add((20, 30), 0, 0, 0)
        bt_h_sizer.Add(self.add_collection_bt, 0, wx.ALL|wx.EXPAND, 0)
        bt_h_sizer.Add(self.cancel_bt, 0, wx.ALL|wx.EXPAND, 0)
        v_sizer.Add(bt_h_sizer, 0, wx.RIGHT|wx.ALIGN_RIGHT, 0)
        self.top_panel.SetSizer(v_sizer)
        top_sizer.Add(self.top_panel, 1, wx.ALL|wx.EXPAND, 0)
        self.SetSizer(top_sizer)
        self.Layout()
        # end wxGlade

    def OnClose(self, event):
        self.Hide()
        self.collection_txt.Clear()
        
    def OnAddCollectionBt(self, event):
        collection_name = self.collection_txt.GetValue().strip()

        # sanitize input
        if collection_name in self.parent.collections.collections:
            wx.MessageDialog(None, "Collection already exists.", "Invalid collection name", wx.OK | wx.ICON_ERROR).ShowModal()
            return
        elif not collection_name:
            wx.MessageDialog(None, "Please provide a collection name.", "Invalid collection name", wx.OK | wx.ICON_ERROR).ShowModal()
            return
        
        # add collection and hide dialog
        self.parent.collections.CreateCollection(collection_name, self.collection_dir_picker.GetPath())
        self.parent.collection_list.InsertStringItem(0, collection_name)
        self.collection_txt.Clear()
        self.parent.screen_grabber_win.SetCollectionList(self.parent.collections.collections.keys())
        self.Hide()



# end of class AddCollectionWin


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    add_collection = AddCollectionWin(None, -1, "")
    app.SetTopWindow(add_collection)
    add_collection.Show()
    app.MainLoop()
