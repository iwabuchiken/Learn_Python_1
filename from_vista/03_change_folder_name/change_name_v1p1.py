import os.path
import os, sys

def change_dirname(dir=os.getcwd(), start_num=1):
  items = os.listdir(dir)
  items_dir = []
  for item in items:
#    if os.path.isdir(item) and not item[:2].isdigit():
    if os.path.isdir(item) and not item.split("_")[0].isdigit():
      items_dir.append(item)
  print items_dir
#  for i in range(len(items_dir[:3])):
#  for i in range(start_num, start_num + len(items_dir)):
  for i in range(len(items_dir)):
#    num_str = str(i)
#    num_str = str(i+1)
#    num_str = str(i+start_num+1)
    num_str = str(i+start_num)
    if len(num_str) < 2: num_str = "0" + num_str
    command = 'ren "%s" "%s"' % \
        (items_dir[i], num_str + "_" + items_dir[i])
#        (items_dir[i], str(i+1) + "_" + items_dir[i])
    print command
#    os.system(command)
#  for item in items_dir:
#    print item
#    print "\t", item + "_2"
#  print items
#  print
#  print items_dir

if __name__ == '__main__':
  argvs = sys.argv
#  start_num = 0
  if len(argvs) < 2: start_num = 5
  else:
    if argvs[1].isdigit(): start_num = int(argvs[1])
    else:
      print "Please input integer. Your input: %s" % argvs[1]
      exit(0)
  change_dirname(start_num)
#  print start_num
#  print argvs
#  print len(argvs)
#  print argvs[0]
#  if len(argvs)
#  change_dirname(start_num=5)