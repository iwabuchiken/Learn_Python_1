"""************************************`
 * sub1_hello_world.py
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

if __name__ == '__main__':
    app = wx.App(False)
    frame = wx.Frame(None, wx.ID_ANY, "Hello World")
    frame.Show(True)
    app.MainLoop()

#print "[LINE:%d]" % inspect.currentframe().f_lineno
#traceback.print_exc(file=sys.stdout)
#   => http://www.python.jp/doc/2.5/lib/traceback-example.html