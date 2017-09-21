import socket
import time
import sys

# Create a TCPP socket
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = 'echo.u-blox.com'
host = 'ciot.it-sgn.u-blox.com'

remote_ip = socket.gethostbyname( host )
port = 5055
BUFSIZ = 1500

print "Host IP: %s, port " % remote_ip, port

server_address = (remote_ip, port)

message = '_____0000:012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'

for x in range(0, 3):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "\r\n Connecting to the socket \r\n"
    print server_address
    sock.connect(server_address)

    for y in range(0, 10):
        # Send data
        print "\nSend: %s " % message
    
        sent = sock.sendto(message, server_address)

       # Receive response
    
        #print "\r\nWaiting to receive"

        starttime = time.time()

        data, server = sock.recvfrom(BUFSIZ) # Size of data received  = 512

        timetaken = time.time() - starttime
    
        print "\r\nReceived Data: %s \r\n" % data
        print "\r\nResponse Time: %s sec" % timetaken
    print "\r\n Closing the socket \r\n"
    sock.close()
        
