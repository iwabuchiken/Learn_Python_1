"""************************************`
 * sub1_draw_line_on_image.py
 * Author: Iwabuchi Ken				*
 * Date: 20120329_084002
 * Aim:								*
 * 	1.
 * <Usage>
 *	1. Run the program
 * <Source>
 * 	1.
 ************************************"""
import os.path
import os
import sys
import inspect
import traceback
import datetime

import Image
import ImageDraw


def get_time_label2():
  t = datetime.datetime.today()
  t1 = [t.year, t.month, t.day, t.hour, t.minute, t.second]
  t2 = [str(item) for item in t1]

  for i in range(len(t2)):
    if len(t2[i]) < 2: t2[i] = "0" + t2[i]

  return "".join(t2[:3]) + "_" + "".join(t2[3:])
#//def get_time_label2()

def open_image(filename):
    """ open image """
#    im = Image.open("lena.ppm")
    im = Image.open(filename)

    """ draw a line """
#    x = im.size[0] / 20       # x coordinate
    x = 0       # x coordinate
    y = im.size[1]  # height of the image
    interval = im.size[0] / 20  # interval of the lines
    draw = ImageDraw.Draw(im)   # setup a draw object
#    draw.line((0,100)+(100,0), fill=(0xbb,0xdd,0xff), width=2)
    """
    draw vertical and horizontal lines
    with certain interval in pixels along the image
    """
    """ lines: vertical """
    while (x < im.size[0]):
#        draw.line((x,0)+(x,100), fill=(0xbb,0xdd,0xff), width=1)
        draw.line((x,0)+(x,y), fill=(0xbb,0xdd,0xff), width=1)
#        x += 10
        x += interval
#        x += im.size[0] / 20
    #//while (x < im.size[0])
    """ lines: horizontal """
    x = im.size[0]
    y = 0
    while (y < im.size[1]):
#        draw.line((x,0)+(x,100), fill=(0xbb,0xdd,0xff), width=1)
        draw.line((0,y)+(x,y), fill=(0xbb,0xdd,0xff), width=1)
#        x += 10
        y += interval
#        x += im.size[0] / 20
    #//while (y < im.size[0])
#    draw.line((0,0)+(0,100), fill=(0xbb,0xdd,0xff), width=5)

    """ save image """
#    trunk, ext  = os.path.splitext(filename)
#    file_out    = trunk + "_" + get_time_label2() + ext
#    file_out_path = os.path.join("tmp", file_out)
#    im.save(file_out_path, "JPEG")

    """ show image """
    im.show()

    """ close imiage """
#    im.close()
#//open_image()

def show_usage():
    print """<Usage>
        sub1_draw_line_on_image.py MA330371.JPG
    """
#//show_usage()

def create_tmp_dir():
    if os.path.exists("tmp") and os.path.isdir("tmp"):
        print "tmp dir exists"
    else:
        print "tmp dir doesn't exist"
        try:
            os.makedirs("tmp")
            print "tmp dir created"
        except Exception, e:
            print "can't create tmp dir"
            print e
    #//if os.path.exists("tmp")

#//create_tmp_dir()

if __name__ == '__main__':
    #debug
    create_tmp_dir()
#    sys.exit(0)

    if len(sys.argv) < 2:
        show_usage()
        sys.exit(0)
    #//if len(sys.argv) < 2
    open_image(sys.argv[1])

#print "[LINE:%d]" % inspect.currentframe().f_lineno
#traceback.print_exc(file=sys.stdout)
#   => http://www.python.jp/doc/2.5/lib/traceback-example.html