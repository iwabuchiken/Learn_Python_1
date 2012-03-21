"""************************************`
 * sub3_sample_editor.py
 * Author: Iwabuchi Ken				*
 * Date: 20120320_201352
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

#class ------------------------------------
class MainWindow(wx.Frame):
    """ a new class of Frame """
#    def __init__(self, parent, title):
    def __init__(self, parent, title, size=(200, 100)):
#        wx.Frame.__init__(self, parent, title=title, size=(200,100))
#        wx.Frame.__init__(self, parent, title=title, size=(400,200))
        wx.Frame.__init__(self, parent, title=title, size=size)
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        
        """ Status bar """
        self.CreateStatusBar() # A Statusbar in the bottom of the window

        """ file menu """
        filemenu = wx.Menu()
        filemenu.Append(wx.ID_ABOUT, "&About", "Information")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "&Exit", "Terminate")

        """ menu bar """
        menuBar = wx.MenuBar()
#        menuBar.Append(filemenu, "&File")
        menuBar.Append(filemenu, "F&ile")

        """ set menu bar """
        self.SetMenuBar(menuBar)

        """ show """
        self.Show(True)
    #//__init__()


if __name__ == '__main__':
    app = wx.App(False)
    frame = MainWindow(None, "Sample Editor")
#    frame.Show(True)
    app.MainLoop()

#print "[LINE:%d]" % inspect.currentframe().f_lineno
#traceback.print_exc(file=sys.stdout)
#   => http://www.python.jp/doc/2.5/lib/traceback-example.html