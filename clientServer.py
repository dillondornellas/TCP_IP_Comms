import socket
import sys 

# Create a TCP/IP socket
#add try here incase of failure
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Then bind() is used to associate the socket with the server address.
local_hostname = socket.gethostname()
ip_address = socket.gethostbyname(local_hostname)
local_fqdn = socket.getfqdn()

server_address = (local_hostname, 10000) 
#print(sys.stderr, 'connecting to %s port %s' % server_address)
print (sys.stderr, "working on %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))

client.bind(server_address)

# Listen for incoming connections
client.listen(1)

while True:
    # Wait for a connection
    print(sys.stderr, 'waiting for a connection')
    connection, client_address = client.accept()

    try:
        print(sys.stderr, 'connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            try:
                data = connection.recv(1024)
                if data:
                    print(sys.stderr, 'received "%s"' % data)
                    print(sys.stderr, 'sending data back to the client')
                    connection.sendall(data)
                else:
                    print(sys.stderr, 'no more data from ', client_address)
                    break
            except:
                break
            
    finally:
        # Clear the connection
        connection.close()