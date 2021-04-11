import socket
import time

class tcpClient:
    def __init__(self):
        self.local_hostname = socket.gethostname()
        self.ip_address = socket.gethostbyname(self.local_hostname)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.initConnection()

    def initConnection(self):
        
        server_address = (self.ip_address, 10000)
        try:
            self.client.connect(server_address)
            print ("connecting to %s with %s" % (self.local_hostname, self.ip_address))
        except:
            print ("Unable to connect to server %s" % (self.ip_address))

    def sendData(self, data):
        for entry in data:
            print ("data: %s" % entry)
            new_data = str(entry).encode('ascii')
            self.client.sendall(new_data)
            time.sleep(1)

    def receiveData(self):
        while True:
            try:
                data = self.client.recv(1024).decode('ascii')
                print(sys.stderr, 'received: %s' % data)
            except:
                print(sys.stderr, 'no more data from ', client_address)
                break

dat = ["15", "22", "21", "26", "25", "19"]

client1 = tcpClient()
client1.sendData(dat)

