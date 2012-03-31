"""************************************`
 * File: sub2_file_open_rplus.py
 * Author: Iwabuchi Ken				*
 * Date: 20120401_074520
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

def func1():
    """ vars """
    fname   = "sub2_test.txt"
#    fout    = file(fname, 'r+')
    fout    = open(fname, 'r+')
#    fout    = file(fname, 'r')

    """ write file """
#    fout.write("xyz\n")

    """ tell the file """
#    print fout.tell()
#    print fout.read()

    """ read file """
    line = fout.readline()
    if line:
#        print line.rstrip()
        print "[LINE:%d]" % inspect.currentframe().f_lineno
#        fout.flush()
        fout.write("abcde")
#        print fout.tell()
#        fout.write("abc")
#        fout.write("ab")
#        print "written"
#        fout.flush()
#        fout.close()
#        fout    = open(fname, 'r+')
#        print fout.tell()
#        print fout.readline()

#    while line:
#        print line.rstrip()
#        line = fout.readline()

    """ write file """
#    fout.write("def")
    
    """ close file """
    fout.close()
#//func1()

if __name__ == '__main__':
    func1()
#print "[LINE:%d]" % inspect.currentframe().f_lineno