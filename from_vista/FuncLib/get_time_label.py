"""
file=v1p1
Modification Time	2011/04/18 8:02:26
"""
import time

def get_time_label():
  t = time.localtime()
  pieces = []
  for item in t:
    digit = str(item)
#    print len(digit)
    if len(digit) < 2: digit = "0" + digit
    pieces.append(digit)
#    pieces.append(str(item))
  print ":".join(pieces[3:6]) + "-" + "/".join(pieces[:3])
#  print "/".join(t[:3]) + "_"
#  label = []
#  for item in t[:3]:
#     piece = ""
#     if len(str(item)) < 2:
#        piece = "0" + str(item)
#     else:
#        piece = str(item)
#     label.append(piece)
#  print "/".join(label)

if __name__ == '__main__':
  get_time_label()
