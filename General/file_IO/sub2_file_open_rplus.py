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
import re

"""
func1()
<Parameters>

<Return>

<Descriptioins>
1. prepare: lines_src[]
2. prepare: lines_header[]
3. write: lines_header[]
"""
def func1():
    """ vars """
#    fin_name   = "sub2_test.txt"
    fin_name   = "sakujyo.c"
#    fout_name   = "sub2_test_out.txt"
    fout_name   = "sakujyo.h"
    fin         = open(fin_name, 'r')
    fout        = open(fout_name, 'r')
    lines_src       = list()
    lines_header    = list()
    regex = re.compile('^((\w|\s)*\((\w|\s)*\))$')

    """ prepare: lines_src """
    line = fin.readline()
    while line:
        result = regex.search(line)
        if result:
#            print result.group()
            lines_src.append(result.group().rstrip())
        line = fin.readline()

    #debug
#    print lines_src, "(%d)" % len(lines_src)

    """ prepare: lines_header[] """
    line = fout.readline()
    regex = re.compile('^((\w|\s)*\((\w|\s)*\));$')
    while line:
        result = regex.search(line)
        if not result:
            lines_header.append(line.rstrip())
        line = fout.readline()
    #debug
#    print "<lines_header>"
#    print lines_header
#    print len(lines_header)

    """ write: lines_header[] 
        1.
        2.
    """
    fout        = open(fout_name, 'w')
    """ 1. lines from the original header file """
    for line in lines_header:
        fout.write(line)
        fout.write('\n')

    """ 2. lines from the source file """
    for line in lines_src:
        fout.write("%s;\n" % line)
#        fout.write('\n')


    """ close file """
    fin.close()
    fout.close()
#//func1()


if __name__ == '__main__':
    func1()
#print "[LINE:%d]" % inspect.currentframe().f_lineno