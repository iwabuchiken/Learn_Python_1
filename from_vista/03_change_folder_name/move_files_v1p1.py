import os.path
import shutil, os

def get_files_flv(dir=os.getcwd()):
  list1 = os.listdir(dir)
  list_files = [item for item in list1 if os.path.isfile(item)]
  files_flv = [item for item in list_files \
              if item.rsplit(".", 1)[1] == "flv" or \
              item.rsplit(".", 1)[1] == "mp3"]
  return files_flv
#  print "path=", os.path.dirname(list_files[0])
#  print "list1[0]=", list1[0]
#  print "path=", os.path.dirname(list1[0])
#  print "path(__file__)=", os.path.dirname(__file__)
#  print __file__
#  print "os.path.dirname(os.path.abspath(__file__))=", \
#    os.path.dirname(os.path.abspath(__file__))
#  print "os.getcwd()=", os.getcwd()
#  print list_files
#  files_flv = [item for item in list_files \
#              if item.rsplit(".", 1)[1] == "flv"]
#  files_flv = [item.rsplit(".", 1)[0] for item in list_files \  

def move_file(file_names, dir=os.getcwd()):
  full_paths = [dir + "\\" + name for name in file_names]
  dst = r"C:\workspaces\ws_audio_video_1\_STORAGE_ws_audio_video_1\files"
  for item in full_paths:
    shutil.move(item, dst)
    print "File moved: %s" % os.path.basename(item)
    print "\t", "From: %s " % os.path.dirname(item)
    print "\t", "To: %s" % dst
  
#  print full_paths
#  for item in full_paths:
#    print item


if __name__ == '__main__':
  names = get_files_flv(dir=os.getcwd())
  move_file(names)
#  print get_files_flv(dir=os.getcwd())
