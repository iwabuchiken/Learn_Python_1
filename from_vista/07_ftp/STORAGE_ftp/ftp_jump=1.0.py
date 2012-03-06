"""
file=
version=1.0
Modification Time	2011/04/25 7:50:53
"""

import os, os.path, sys
from ftplib import FTP
from cStringIO import StringIO
from datetime import datetime

if __name__ == '__main__':
  dtemp = os.getenv("TEMP") or os.getenv("TMP") or "C:\\"
  print dtemp
  INP = 'upload.inp'
  LOG = 'upload.log'
  log_name = os.path.join(dtemp, LOG)
  print log_name
  os.path.exists(log_name) and os.remove(log_name)
  inp_name = os.path.join(dtemp, INP)
  print inp_name

  #02
  server = "183.181.0.54"
  user = "user1"
  passw = "seeitthrough"
  try:
    ftp = FTP(server)
    print "Connected to the server: %s" % server
  except Exception,e:
    print e

  try:
    ftp.login(user, passw)
    print "Logged in"
  except Exception,e:
    print e

  print ftp.dir()

  sys.stdout = StringIO()
  try:
    ftp.dir()
  except Exception,e:
    print e
  sys.stdout.getvalue()


  try:
    ftp.close()
    print "Connection closed"
  except Exception,e:
    print e

  print "Program complete. See you."