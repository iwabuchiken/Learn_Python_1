"""************************************`
 * sub2_windows_sizer.py
 * Author: Iwabuchi Ken				*
 * Date: 20120321_075839
 * Aim:								*
 * 	1.
 * <Usage>
 *	1. Run the program
 * <Source>
 * 	1.
 ************************************"""
import os
import sys
import inspect
import traceback

import wx

#class ======================================
class MainWindow(wx.Frame):
    """ a new class of Frame """
    def __init__(self, parent, title, size=(200, 100)):
        self.dirname    = ''
#        self.dirname    = 'c:\\'
        wx.Frame.__init__(self, parent, title=title, size=size)
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        """ Status bar """
        self.CreateStatusBar() # A Statusbar in the bottom of the window

        """ file menu """
        filemenu = wx.Menu()
        menuOpen   = filemenu.Append(wx.ID_OPEN, "&Open", "Open a file")
        menuAbout   = filemenu.Append(wx.ID_ABOUT, "&About", "Information")
        filemenu.AppendSeparator()
        menuExit    = filemenu.Append(wx.ID_EXIT, "&Exit", "Terminate")

        """ option menu """
        optmenu = wx.Menu()
        optSetDir   = optmenu.Append(
                wx.ID_PROPERTIES, "Set &directory",
                "Set the default directory")        

        """ menu bar """
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        menuBar.Append(optmenu, "&Option")
#        menuBar.Append(filemenu, "F&ile")

#        menuBar2    = wx.MenuBar()
#        menuBar2.Append(optmenu, "Op&tion")

        """ set menu bar """
        self.SetMenuBar(menuBar)
#        self.SetMenuBar(menuBar2)

        """ create sizers """
#        self.sizer2     = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer2     = wx.BoxSizer(wx.VERTICAL)
        self.buttons    = []
        for i in range(0,6):
            self.buttons.append(
#                    wx.Buttons(self, -1, "Button &" + str(i)))
                    wx.Button(self, -1, "Button &" + str(i)))
#            self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)
            self.sizer2.Add(self.buttons[i], 1, wx.SHAPED)
        #for i in range(0,6)

        self.sizer  = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 1, wx.EXPAND)
#        self.sizer.Add(self.sizer2, 0, wx.EXPAND)
#        self.sizer.Add(self.sizer2, 0, wx.SHAPED)
        self.sizer.Add(self.sizer2, 0, wx.ALIGN_RIGHT)

        """ set sizer """
#        self.SetSizer(self.sizer2)
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
#        self.sizer2.Fit(self)

        """ set events """
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Bind(wx.EVT_MENU, self.OnSetDir, optSetDir)
#        self.Bind(wx.EVT_MENU, self.OnSetDir, self.buttons[0])

        """ show """
        self.Show()
#        self.Show(True)
    #//__init__()

    def OnAbout(self, e):
#        dlg  = wx.MessageDialog(self, "Small Text Editor", "About Sample Editor", wx.OK)
        print "OnAbout"
        dlg  = wx.MessageDialog(self, "Small Text Editor", "About Sample Editor")
        dlg.ShowModal()
        dlg.Destroy()
    #//OnAbout()

    def OnExit(self, e):
        self.Close(True)
    #//OnExit()

    def OnOpen(self, e):
        dlg = wx.FileDialog(
                self, "choose a file",
                self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()
        #//if dlg.ShowModal() == wx.ID_OK
    #//OnOpen()

    """ OnSetDir()
    1. Set the directory.
    """
    def OnSetDir(self, e):
        """ Show the entry dialog """
        dlg = wx.TextEntryDialog(
            self, "Enter your directory of choice",
            "Choose directory", "Default")
        if dlg.ShowModal() == wx.ID_OK:
            """ Display the input in the message dialog """
            """ Set the dialog """
            m_dlg = wx.MessageDialog(self,
                "Your choice: %s" % dlg.GetValue(),
                "Message")
            """ show the dialog """
            m_dlg.ShowModal()
            """ set 'dirname' variable """
            self.dirname    = dlg.GetValue()
            """ close the message dialog """
            m_dlg.Destroy()
            
        """ close the entry dialog """
        dlg.Destroy()

#            self.log.WriteText("Your choice: %s" % dlg.GetValue())
        #//if dlg.ShowModal() == wx.ID_OK
    #//OnSetDir()
#//class MainWindow(wx.Frame)

if __name__ == '__main__':
    app = wx.App(False)
    frame = MainWindow(None, "Sample Editor")
    app.MainLoop()


#print "[LINE:%d]" % inspect.currentframe().f_lineno
#traceback.print_exc(file=sys.stdout)
#   => http://www.python.jp/doc/2.5/lib/traceback-example.html