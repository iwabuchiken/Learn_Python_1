#!/usr/local/python/bin/python
#coding:utf-8
import ftp_jump_sample
import get_time_label
"""
file=v1p1
Modification Time	2011/04/25 9:56:42
"""

print "Content-Type: text/html\n"
print "\n"

def do_numbering():
  f1 = file("ftp_jump_sample.py", "r")

  content_f1 = f1.readlines()

  text = "<pre>\n"
  i = 0
  for line in content_f1:
    i_str = str(i)
    if len(i_str) < 2: i_str = "0" + i_str
    line = "\t" + "<span>%s:</span>" % i_str + "\t" + line
    text += line
    i += 1
  text += "\n</pre>"
  f1.close()
  print text

if __name__ == '__main__':
  do_numbering()