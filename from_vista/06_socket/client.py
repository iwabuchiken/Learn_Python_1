#client.py
import socket
#host = '127.0.0.1'
host = '183.181.0.54'
port = 3794

def do_client():
  clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  clientsock.connect((host,port))
  print "Socket connected => %s:%d" % (host, port)

  while True:
    print 'Type message...'
    c_msg = raw_input()
    if c_msg == '':
      break
    print 'Wait...'

    clientsock.sendall(c_msg)
    rcvmsg = clientsock.recv(1024)
    print 'Received -> %s' % (rcvmsg)
    if rcvmsg == '':
      break

  clientsock.close()


if __name__ == '__main__':
  do_client()
