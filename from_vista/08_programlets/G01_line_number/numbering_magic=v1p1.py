#!/usr/local/python/bin/python
#file=v1p1
import ftp_jump_sample

f1 = file("ftp_jump_sample.py", "r")
f2 = file("ftp_jump_sample.py.copy", "w")

content_f1 = f1.read()
for line in content_f1:
  line = "00:" + line
  f2.write(line)
#print content_f1.__class__
#f2.write(content_f1)
f1.close()
f2.close()
print __file__