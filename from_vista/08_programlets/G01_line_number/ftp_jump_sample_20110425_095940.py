<pre>
	<span>00:</span>	import os, os.path, sys
	<span>01:</span>	from ftplib import FTP
	<span>02:</span>	from cStringIO import StringIO
	<span>03:</span>	from datetime import datetime
	<span>04:</span>	
	<span>05:</span>	if __name__ == '__main__':
	<span>06:</span>	  dtemp = os.getenv("TEMP") or os.getenv("TMP") or "C:\\"
	<span>07:</span>	  print dtemp
	<span>08:</span>	  INP = 'upload.inp'
	<span>09:</span>	  LOG = 'upload.log'
	<span>10:</span>	  log_name = os.path.join(dtemp, LOG)
	<span>11:</span>	  print log_name
	<span>12:</span>	  os.path.exists(log_name) and os.remove(log_name)
	<span>13:</span>	  inp_name = os.path.join(dtemp, INP)
	<span>14:</span>	  print inp_name
	<span>15:</span>	
	<span>16:</span>	  #02
	<span>17:</span>	  server = "183.181.0.54"
	<span>18:</span>	  user = "user1"
	<span>19:</span>	  passw = "seeitthrough"
	<span>20:</span>	  try:
	<span>21:</span>	    ftp = FTP(server)
	<span>22:</span>	    print "Connected to the server: %s" % server
	<span>23:</span>	  except Exception,e:
	<span>24:</span>	    print e
	<span>25:</span>	
	<span>26:</span>	  try:
	<span>27:</span>	    ftp.login(user, passw)
	<span>28:</span>	    print "Logged in"
	<span>29:</span>	  except Exception,e:
	<span>30:</span>	    print e
	<span>31:</span>	
	<span>32:</span>	  print ftp.dir()
	<span>33:</span>	
	<span>34:</span>	  sys.stdout = StringIO()
	<span>35:</span>	  try:
	<span>36:</span>	    ftp.dir()
	<span>37:</span>	  except Exception,e:
	<span>38:</span>	    print e
	<span>39:</span>	  sys.stdout.getvalue()
	<span>40:</span>	
	<span>41:</span>	
	<span>42:</span>	  try:
	<span>43:</span>	    ftp.close()
	<span>44:</span>	    print "Connection closed"
	<span>45:</span>	  except Exception,e:
	<span>46:</span>	    print e
	<span>47:</span>	
	<span>48:</span>	  print "Program complete. See you."
</pre>