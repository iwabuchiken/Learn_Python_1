#!/usr/local/python/bin/python
import socket

def do_socket():
  host = '127.0.0.1'
  port = 3794
  serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  print serversock
  #print dir(serversock)

  serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  try:
    serversock.bind((host,port))
  except Exception, e:
    print e
  print "Bind successful: %s:%d" % (host, port)

  serversock.listen(1)

  print 'Waiting for connections...'
  clientsock, client_address = serversock.accept()

  #print clientsock.__class__
  #print client_address.__class__
  print clientsock
  print client_address

  log_file = "log_socket.log"
  f = open(log_file, "w")
  while True:
    rcvmsg = clientsock.recv(2000)
  #  rcvmsg = clientsock.recv()
    print 'Received -> %s' % (rcvmsg)
    f.write(rcvmsg)
    if rcvmsg == '':
      break
    print 'Type message...'
    s_msg = raw_input()
    f.write(s_msg)

    if s_msg == '':
      break
    print 'Wait...'
    result = clientsock.sendall(s_msg)
    print result
  clientsock.close()
  f.close()

if __name__ == '__main__':
  do_socket()