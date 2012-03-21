"""************************************`
 * sub1_first_example.py
 * Author: Iwabuchi Ken				*
 * Date: 20120321_105947
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

class ExampleFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        panel = wx.Panel(self)
        self.quote = wx.StaticText(
                    panel, label="Your quote: ",
                    pos=(20, 30))
        self.Show()
    #//__init__()
#//class ExampleFrame(wx.Frame)

if __name__ == '__main__':
    app = wx.App(False)
    ExampleFrame(None)
    app.MainLoop()

#print "[LINE:%d]" % inspect.currentframe().f_lineno
#traceback.print_exc(file=sys.stdout)
#   => http://www.python.jp/doc/2.5/lib/traceback-example.html