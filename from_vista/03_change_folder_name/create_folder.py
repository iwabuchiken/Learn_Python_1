import os, time, sys

def create_newfolder(num=5):
  d = time.localtime()
  d_str = []
  for item in d:
    elem = str(item)
    if len(elem) < 2: elem = "0" + elem
    d_str.append(elem)  
  for i in range(1,num+1):
    folder_name = "new_folder_%s_%d" % (("".join(d_str[:6])), i)
#    print folder_name
    command = "md %s" % folder_name
    os.system(command)
    print "New folder created: %s" % folder_name
#  print "New folder created: %s" % folder_name

if __name__ == '__main__':
  argvs = sys.argv
  if len(argvs) <= 1: create_newfolder()#num = 5
  else:
    if argvs[1].isdigit(): create_newfolder(int(argvs[1]))#num = int(argvs[1])
    else:
      print "param is not an integer. Your input: %s" % argvs[1]
#      create_newfolder()#num = 0
#  print num
#  print argvs[0]
#  print len(argvs)

#  print argvs[1]
#  create_newfolder(num=5)