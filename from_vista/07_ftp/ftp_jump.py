"""
file=
version=1.0
Modification Time	2011/04/25 7:50:53
Modification Time	2011/04/29 18:01:35
"""

import os, os.path, sys
from ftplib import FTP
from cStringIO import StringIO
from datetime import datetime

if __name__ == '__main__':
  #01 setup
  dtemp = os.getenv("TEMP") or os.getenv("TMP") or "C:\\"
  INP = 'upload.inp'
  LOG = 'upload.log'
  log_name = os.path.join(dtemp, LOG)
  os.path.exists(log_name) and os.remove(log_name)
  inp_name = os.path.join(dtemp, INP)
  
  #02
  server = "183.181.0.54"
  user = "user1"
  passw = "seeitthrough"
  #connect to the server
  try:
    ftp = FTP(server)
    print "Connected to the server: %s" % server
  except Exception,e: print e

  #log in
  try:
    ftp.login(user, passw)
    print "Logged in"
  except Exception,e: print e

  print ftp.dir()
  ftp.cwd("/var/www/cgi-bin/")
  f = file("console.txt", "r")
  storlines("STOR console.txt", f)

#  # get data
#  f = file("console.txt")
#  print eval()