"""************************************`
 * foo.py
 * Author: Iwabuchi Ken				*
 * Date: 20120324_071953
 * Aim:								*
 * 	1.
 * <Usage>
 *	1. Run the program
 * <Source>
 * 	1.
 ************************************"""
from distutils.core import setup

setup(name='foo',
        version='1.0',
        py_modules=['foo'])

if __name__ == '__main__':
    print __file__

#print "[LINE:%d]" % inspect.currentframe().f_lineno
#traceback.print_exc(file=sys.stdout)
#   => http://www.python.jp/doc/2.5/lib/traceback-example.html