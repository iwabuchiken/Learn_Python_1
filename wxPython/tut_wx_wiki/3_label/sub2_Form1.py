"""************************************`
 * sub2_Form1.py
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

class Admin:
    def __init__(self, frame):
        self.frame = frame
    #//__init__()
#    def setMenuBar(self, frame):
    def setMenuBar(self):
        """ menu """
        fileMenu = wx.Menu()
        menuExit = fileMenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        """ menu bar """
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu,"&File") # Adding the "filemenu" to the MenuBar
        frame.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        """ bind """
        frame.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        """ return """
        return frame
    #//setMenuBar()

    def OnExit(self, e):
        frame.Close(True)
    #//OnExit()
#//class Admin

class ExamplePanel(wx.Panel):
    #==================================
    #   Class: init
    #==================================
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        #==================================
        #   Tool bar
        #   
        #==================================
#        """ menu """
#        fileMenu = wx.Menu()
#        menuExit = fileMenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")
#
#        """ menu bar """
#        menuBar = wx.MenuBar()
#        menuBar.Append(fileMenu,"&File") # Adding the "filemenu" to the MenuBar
#        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        #==================================
        #   Panel items
        #==================================
        """ 1. controls """
        self.quote = wx.StaticText(
                    self, label="Your quote: ",
                    pos=(20, 30))
        self.logger = wx.TextCtrl(self,
                    pos=(300,20), size=(200,300),
                    style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.button = wx.Button(self,
                    label="Save", pos=(200,325))
        """ 2. Bind the button """
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)

        """ 3. edit control """
        self.lblname = wx.StaticText(self, label="Your name :", pos=(20,60))
        self.editname = wx.TextCtrl(self, value="Enter here your name", pos=(150,60), size=(140,-1))
        self.lblname2 = wx.StaticText(self, label="Hit any key :", pos=(20,120))
        self.editname2 = wx.TextCtrl(self, value="Hit any key", pos=(150,120), size=(140,-1))

        """ 4. bind controls """
#        self.Bind(wx.EVT_TEXT, self.EvtText, self.editname)
        self.editname.Bind(wx.EVT_TEXT, self.EvtText)
#        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editname)
        self.editname2.Bind(wx.EVT_CHAR, self.EvtChar)

        """ 5. control: combobox """
        self.sampleList = ['friends', 'advertise', 'web search', 'Yello Pages']
        self.lblhear = wx.StaticText(self, label="How did you hear from us ?", pos=(20, 90))
#        self.edithear = wx.ComboBox(self, pos=(150,90), size=(135, 90), choices=self.sampleList, style=wx.CB_DROPDOWN)
        self.edithear = wx.ComboBox(self, pos=(150,90), size=(135, 90), choices=self.sampleList, style=wx.CB_DROPDOWN)

        """ Bind combobox """
#        self.edithear.Bind(wx.EVT_TEXT, self.EvtText)
        self.edithear.Bind(wx.EVT_COMBOBOX, self.EvtComboBox)

        """ 6. Checkbox """
        self.insure = wx.CheckBox(self, label="Do you wnat Insured Shipment ?", pos=(20,180))
        self.insure.Bind(wx.EVT_CHECKBOX, self.EventCheckBox)

        """ 7. RadioBox """
        radioList = ['blue', 'red', 'yellow']
        self.rb = wx.RadioBox(self, label="What color ?", pos=(20, 210), choices=radioList, majorDimension=3, style=wx.RA_SPECIFY_COLS)
        self.rb.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox)

        """ Show the panel """
        self.Show()
    #//__init__()


    def OnClick(self, event):
        self.logger.AppendText(
                "Click on object with Id %d \n" % event.GetId())
                

    #//OnClick()

    #==================================
    #   Class methods
    #==================================
    def EvtText(self, event):
#        pass
        self.logger.AppendText(
                'EvtText: %s\n' % event.GetString())
    #//EvtText()

    def EvtChar(self, event):
        self.logger.AppendText('EvtChar: %d\n' % event.GetKeyCode())
    #//EvtChar()

    def EvtComboBox(self, event):
        self.logger.AppendText('EventComboBox: %s \n' % event.GetString())
    #//EvtComboBox()

    def EventCheckBox(self, event):
        self.logger.AppendText('EventCheckBox: %d \n' % event.Checked())
    #//EventCheckBox()

    def EvtRadioBox(self, event):
#        self.logger.AppendText('EventRadioBox: %d \n' % event.GetInt())
        self.logger.AppendText('EventRadioBox: %s \n' % event.GetString())
    #//EvtRadioBox()
#//class ExampleFrame(wx.Frame)

if __name__ == '__main__':
    """ create an App """
    app = wx.App(False)
    """ create a Frame """
#    frame = wx.Frame(None)
    frame = wx.Frame(None, size=(1000,500))

    """ set menu bar """
#    frame = Admin(frame).setMenuBar(frame)
    frame = Admin(frame).setMenuBar()

    """ generate a Panel """
    panel = ExamplePanel(frame)
    frame.Show()

    """ main loop """
    app.MainLoop()

#print "[LINE:%d]" % inspect.currentframe().f_lineno
#traceback.print_exc(file=sys.stdout)
#   => http://www.python.jp/doc/2.5/lib/traceback-example.html