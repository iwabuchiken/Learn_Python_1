import os, sys

def change_dirname(start_num, dir=os.getcwd()):
#  print dir
#  print start_num
  items = os.listdir(dir)
  items_dir = []
  for item in items: # prepare directory name list
    if os.path.isdir(item) and not item.split("_")[0].isdigit():
      items_dir.append(item)
  print items_dir
  for i in range(len(items_dir)): # change names
    num_str = str(i+start_num)
    if len(num_str) < 2: num_str = "0" + num_str
    command = 'ren "%s" "%s"' % \
        (items_dir[i], num_str + "_" + items_dir[i])
    print command
    os.system(command)

if __name__ == '__main__':
  argvs = sys.argv
#  if len(argvs) < 2: num = 5
  if len(argvs) < 2:
    print "Plese input args for starting number"
    exit(0)
  else:
    if argvs[1].isdigit(): num = int(argvs[1])
    else:
      print "Please input integer. Your input: %s" % argvs[1]
      exit(0)
  change_dirname(start_num=num)
