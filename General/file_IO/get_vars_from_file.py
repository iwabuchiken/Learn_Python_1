"""************************************`
 * File: get_vars_from_file.py
 * Author: Iwabuchi Ken				*
 * Date: 20120310_093920
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


if __name__ == '__main__':
    """ vars """
    f       = file("data.dat")  #   data file
    exts    = list()            #   hold extensions

    """ read lines """
    line = f.readline()
    while line:
        print line
#        exts.append(line.rstrip('rn'))
        exts.append(line.rstrip('\r\n'))
#        exts.append(line.rstrip())
        line = f.readline()
    #//while (f.readline())

    """ show exts """
    print exts
#print "[LINE:%d]" % inspect.currentframe().f_lineno