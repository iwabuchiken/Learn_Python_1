#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.5 (standalone edition) on Thu Mar 29 14:57:40 2012

import wx

# begin wxGlade: extracode
# end wxGlade


class MyFrame1(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame1.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)

#        self.size = (200, 200)
        # Menu Bar
        self.frame_2_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.NewId(), "New", "", wx.ITEM_NORMAL)
        menuExit = wxglade_tmp_menu.Append(
                    wx.NewId(), "Exit", "", wx.ITEM_NORMAL)
        self.frame_2_menubar.Append(wxglade_tmp_menu, "File")
        wxglade_tmp_menu = wx.Menu()
        self.frame_2_menubar.Append(wxglade_tmp_menu, "Config")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.NewId(), "Version", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.NewId(), "Help", "", wx.ITEM_NORMAL)
        self.frame_2_menubar.Append(wxglade_tmp_menu, "Options")
        self.SetMenuBar(self.frame_2_menubar)
        # Menu Bar end
        self.frame_2_statusbar = self.CreateStatusBar(1, 0)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

        """ debug: add menu: Debug """
        wxglade_tmp_menu = wx.Menu()        
        menuDebug = wxglade_tmp_menu.Append(
                    wx.NewId(), "dir()", "", wx.ITEM_NORMAL)
        self.frame_2_menubar.Append(wxglade_tmp_menu, "Debug")

        """ Bind """
        self.Bind(wx.EVT_MENU, self.OnDebug, menuDebug)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        """ debug: show dir(): wx.Frame """
#        print
#        print dir(wx.Frame)
        
        """ debug: show dir() """
##        print dir(self.frame_2_menubar)
##        print self.frame_2_menubar.GetMenus()
#        for item in self.frame_2_menubar.GetMenus():
#            print item, "//",  type(item)
        """ debug: GetMenu() """
#        print
#        print self.frame_2_menubar.GetMenu(0)
#        print
#        print dir(self.frame_2_menubar.GetMenu(0))
#        print self.frame_2_menubar.GetMenu(0).GetLabel()   #=> TypeError: Required argument 'id' (pos 2) not found
#        print self.frame_2_menubar.GetMenu(0).GetLabelText() #=> TypeError: Required argument 'itemid' (pos 2) not found
#        print self.frame_2_menubar.GetMenu(0).Title
#        print
#        print self.frame_2_menubar.GetMenu(0).GetMenuItems()
#        print
#        print self.frame_2_menubar.GetMenu(0).FindItemByPosition(0)
#        print
#        print self.frame_2_menubar.GetMenu(0).FindItemByPosition(0).GetItemLabel()
#        print type(self.frame_2_menubar.GetMenu(0).FindItemByPosition(1))
        anItem = self.frame_2_menubar.GetMenu(0).FindItemByPosition(0)
        print anItem, "/", type(anItem), "/", anItem.GetLabel()
        print menuExit, "/", type(menuExit), "/", menuExit.GetLabel()

    def __set_properties(self):
        # begin wxGlade: MyFrame1.__set_properties
        self.SetTitle("Frame with notebook")
        self.frame_2_statusbar.SetStatusWidths([-1])
        # statusbar fields
        frame_2_statusbar_fields = ["Creadted with wxGlade!"]
        for i in range(len(frame_2_statusbar_fields)):
            self.frame_2_statusbar.SetStatusText(frame_2_statusbar_fields[i], i)
        # end wxGlade

        """ debug: SetSize() """
        self.SetSize(wx.Size(400, 200))

    def __do_layout(self):
        # begin wxGlade: MyFrame1.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer_1)
#        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def do_something(self):
        """Documentation"""
        print "something"
    #//def do_something(self):

    def OnDebug(self, event):
#        print wx.Menu().FindItemByPosition(0)
#        print dir(wx.Menu().FindItemByPosition(0))
        print dir(self.frame_2_menubar)
    #//OnDebug()

    def OnExit(self, e):
        self.Close(True)
    #//OnExit()

# end of class MyFrame1
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_2 = MyFrame1(None, -1, "sub1.py")
    app.SetTopWindow(frame_2)
    frame_2.Show()
    app.MainLoop()
