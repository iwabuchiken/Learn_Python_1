#!/usr/local/python/bin/python
import ftp_jump_sample
import get_time_label
"""
file=v1p2
Modification Time	2011/04/25 9:51:32
"""
def do_numbering():
  f1 = file("ftp_jump_sample.py", "r")
  f2 = file("ftp_jump_sample_%s.py" % \
          get_time_label.get_time_label(), "w")

  content_f1 = f1.readlines()
  f2.write("<pre>\n")
  for line in content_f1:
    line = "\t" + "00:" + "\t" + line
    f2.write(line)
  #print content_f1.__class__
  #f2.write(content_f1)
  f2.write("\n</pre>")
  f1.close()
  f2.close()
  print __file__

if __name__ == '__main__':
  do_numbering()