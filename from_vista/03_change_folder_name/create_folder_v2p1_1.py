#file=v2p1
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

def get_files_flv(dir=):
def create_newfolder2():
  pass



if __name__ == '__main__':
  argvs = sys.argv

  def_create_new_folder_2.def_test()
  print __file__
