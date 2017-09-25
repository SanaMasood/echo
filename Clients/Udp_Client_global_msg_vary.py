import socket
import time
import sys
import string
import random

#random Data generator
def id_generator(chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Create a TCPP socket
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = 'echo.u-blox.com'
server = 'ciot.it-sgn.u-blox.com'

remote_ip = socket.gethostbyname( server )
port = 5050
BUFSIZE = 1500

print "Server IP: %s, port " % remote_ip, port

server_address = (remote_ip, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(server_address)
print "\r\nConnecting to the socket with UDP Server\r\n"

test_status = 'Pass'

for x in range(1, 1473):
    size=x
    message=id_generator();
    for y in range(0, 1):
        # Send data
        print "Sending Data of size %s through socket"  % x
  
        sent = sock.sendto(message, server_address)

        starttime = time.time()
        
        #time.sleep(3)

        data, server = sock.recvfrom(BUFSIZE) # Data received from Server

        timetaken = time.time() - starttime
        
        if data == message:
          print "%s :: Recieved data size and contents match"%test_status
        else:
          test_status = "Error"
          print "%s :: Recieved data size and contents mismatch"%test_status
          print "\nSent: %s \n" % message 
          print "\nreceived: %s \n" % data
          raise Exception          
    
        print "Response Time: %s sec\n\n\n" % timetaken
      
print "\r\n Closing the socket \r\n"
sock.close()
