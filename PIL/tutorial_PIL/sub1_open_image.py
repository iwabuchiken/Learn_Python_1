"""************************************`
 * sub1_open_image
 * Author: Iwabuchi Ken				*
 * Date: 20120323_145719
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

import Image

def open_image():
    """ open image """
    im = Image.open("lena.ppm")

    """ show image """
    im.show()

#//open_image()

if __name__ == '__main__':
    open_image()

#print "[LINE:%d]" % inspect.currentframe().f_lineno
#traceback.print_exc(file=sys.stdout)
#   => http://www.python.jp/doc/2.5/lib/traceback-example.html