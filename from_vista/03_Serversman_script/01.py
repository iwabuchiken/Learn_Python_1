#!/usr/local/python/bin/python
import datetime
import time

print "Content-Type: text/html\n"
print "\n"

print __file__, "<br/>", "<br/>"

clock = time.localtime()
clock_str = [str(item) for item in clock]
clock_fin = []
for item in clock_str:
  if len(item) < 2: clock_fin.append("0" + item)
  else: clock_fin.append(item)
label = ":".join(clock_fin[3:6]) + "-"\
    + "/".join(clock_fin[:3])
print label