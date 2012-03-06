#file=v2p1
"""
18:27:33-2011/04/21
How to use this module:
  1. Copy this file to any directory where you located your flv files
  2. Run the file, then,
  3. You will see folder(s) created with the names corresponding to
    each flv file
  4. Now you are done.
"""
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

def get_files_flv(dir=os.getcwd()):
  list1 = os.listdir(dir)
  list_files = [item for item in list1 if os.path.isfile(item)]
#  files_flv = [item for item in list_files \
#              if item.rsplit(".", 1)[1] == "flv"]
  files_flv = [item.rsplit(".", 1)[0] for item in list_files \
              if item.rsplit(".", 1)[1] == "flv"]
  return files_flv
#  print list1
#  print list_files
#  print files_flv

  pass

def get_folders(dir=os.getcwd()):
  list1 = os.listdir(dir)
  list_dirs = [item for item in list1 if os.path.isdir(item)]
  return list_dirs
#  print list1
#  print list_dirs
#  pass

def create_newfolder2():
  files_flv = get_files_flv()
  folders = get_folders()

  for item in files_flv:
    if not item in folders:
      command = 'md "%s"' % item
      print command
      os.system(command)

if __name__ == '__main__':
  argvs = sys.argv
#  print get_files_flv()
#  create_newfolder2()
#  print get_folders(dir=os.getcwd())
  create_newfolder2()