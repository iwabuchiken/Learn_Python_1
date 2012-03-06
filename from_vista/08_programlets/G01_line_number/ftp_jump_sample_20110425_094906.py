00:import os, os.path, sys
00:from ftplib import FTP
00:from cStringIO import StringIO
00:from datetime import datetime
00:
00:if __name__ == '__main__':
00:  dtemp = os.getenv("TEMP") or os.getenv("TMP") or "C:\\"
00:  print dtemp
00:  INP = 'upload.inp'
00:  LOG = 'upload.log'
00:  log_name = os.path.join(dtemp, LOG)
00:  print log_name
00:  os.path.exists(log_name) and os.remove(log_name)
00:  inp_name = os.path.join(dtemp, INP)
00:  print inp_name
00:
00:  #02
00:  server = "183.181.0.54"
00:  user = "user1"
00:  passw = "seeitthrough"
00:  try:
00:    ftp = FTP(server)
00:    print "Connected to the server: %s" % server
00:  except Exception,e:
00:    print e
00:
00:  try:
00:    ftp.login(user, passw)
00:    print "Logged in"
00:  except Exception,e:
00:    print e
00:
00:  print ftp.dir()
00:
00:  sys.stdout = StringIO()
00:  try:
00:    ftp.dir()
00:  except Exception,e:
00:    print e
00:  sys.stdout.getvalue()
00:
00:
00:  try:
00:    ftp.close()
00:    print "Connection closed"
00:  except Exception,e:
00:    print e
00:
00:  print "Program complete. See you."