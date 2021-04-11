import socket
import sys 

# create a TCP/IP socket
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(sys.stderr, 'socket created')
except socket.error:
    print(sys.stderr, 'failed to create socket')

# associate the socket with the server address.
local_hostname = socket.gethostname()
ip_address = socket.gethostbyname(local_hostname)
local_fqdn = socket.getfqdn()

server_address = (local_hostname, 10000) 
print (sys.stderr, 'working on %s (%s) with %s' % (local_hostname, local_fqdn, ip_address))

client.bind(server_address)

# listen for incoming connections
client.listen(1)

while True:
    # wait for a connection
    print(sys.stderr, 'waiting for a connection')
    connection, client_address = client.accept()
    try:
        print(sys.stderr, 'connection from', client_address)
        # receive the data and retransmit it back
        while True:
            try:
                data = connection.recv(1024)
                if data:
                    print(sys.stderr, 'received: "%s"' % data)
                    print(sys.stderr, 'sending data back to the client')
                    connection.sendall(data)
                else:
                    print(sys.stderr, 'no more data from ', client_address)
                    break
            except:
                break       
    finally:
        # clear the connection
        connection.close()