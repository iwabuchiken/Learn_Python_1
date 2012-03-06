"""
file=v1p1
file=v1p1
Modification Time	2011/04/18 8:02:26
Modification Time	2011/04/25 9:41:04
"""
import time

def get_time_label():
  t = time.localtime()
  t_str = [str(item) for item in t]
  pieces = []
  for item in t_str:
    if len(item) < 2: item = "0" + item
    pieces.append(item)
  return "".join(pieces[:3]) + "_" + "".join(pieces[3:6])

if __name__ == '__main__':
  get_time_label()
