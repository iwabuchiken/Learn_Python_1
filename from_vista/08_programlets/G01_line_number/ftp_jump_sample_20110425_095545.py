<pre>
	00:	import os, os.path, sys
	01:	from ftplib import FTP
	02:	from cStringIO import StringIO
	03:	from datetime import datetime
	04:	
	05:	if __name__ == '__main__':
	06:	  dtemp = os.getenv("TEMP") or os.getenv("TMP") or "C:\\"
	07:	  print dtemp
	08:	  INP = 'upload.inp'
	09:	  LOG = 'upload.log'
	10:	  log_name = os.path.join(dtemp, LOG)
	11:	  print log_name
	12:	  os.path.exists(log_name) and os.remove(log_name)
	13:	  inp_name = os.path.join(dtemp, INP)
	14:	  print inp_name
	15:	
	16:	  #02
	17:	  server = "183.181.0.54"
	18:	  user = "user1"
	19:	  passw = "seeitthrough"
	20:	  try:
	21:	    ftp = FTP(server)
	22:	    print "Connected to the server: %s" % server
	23:	  except Exception,e:
	24:	    print e
	25:	
	26:	  try:
	27:	    ftp.login(user, passw)
	28:	    print "Logged in"
	29:	  except Exception,e:
	30:	    print e
	31:	
	32:	  print ftp.dir()
	33:	
	34:	  sys.stdout = StringIO()
	35:	  try:
	36:	    ftp.dir()
	37:	  except Exception,e:
	38:	    print e
	39:	  sys.stdout.getvalue()
	40:	
	41:	
	42:	  try:
	43:	    ftp.close()
	44:	    print "Connection closed"
	45:	  except Exception,e:
	46:	    print e
	47:	
	48:	  print "Program complete. See you."
</pre>