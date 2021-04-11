import socket
import time
import sys 

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
        #print ("data: %s" % data)
        new_data = str(data)
        self.client.send(bytes(data,'ascii'))

    def receiveData(self):
        while True:
            try:
                data = self.client.recv(1024).decode('ascii')
                print(sys.stderr, 'received: %s' % data)
                break
            except:
                print(sys.stderr, 'echo not received', client_address)
                break


dat = '[11][0.6687949706053933, 0.9866176447505118, 0.3482928666204528]\x00[22][9, -16, -28]\x00[33][1, 1, 1]\x00[11][0.882335774796032, 0.33114033843835633, 0.1579493784169541]\x00[22][-4, -18, -17]\x00[33][0, 0, 0]\x00[11][0.3433161171529475, 0.23603251725235308, 0.49143138904346184]\x00[22][4, 17, -30]\x00[33][1, 0, 1]\x00[11][0.33408755020101877, 0.23387336003172676, 0.9174727724578773]\x00[22][8, -4, -11]\x00[33][0, 0, 1]\x00[11][0.41577553052979666, 0.47894390322286884, 0.7338557598861271]\x00[22][6, 15, 3]\x00[33][0, 0, 0]\x00[11][0.17856591909478592, 0.6400568604819764, 0.3958512065334282]\x00[22][-9, -13, -11]\x00[33][0, 1, 1]\x00[11][0.813781998790508, 0.37802430505925766, 0.424373807370117]\x00[22][5, -6, -21]\x00[33][0, 1, 0]\x00[11][0.8992240626200263, 0.20096023406062724, 0.4298957057137537]\x00[22][0, -4, 3]\x00[33][0, 0, 1]\x00[11][0.3393822880909392, 0.28125673261356143, 0.43181603402861146]\x00[22][-5, 2, -21]\x00[33][0, 0, 0]\x00[11][0.9357641322644188, 0.6131036709069413, 0.9235705177483603]\x00[22][-9, -14, 13]\x00[33][1, 1, 1]\x00'

client1 = tcpClient()
client1.sendData(dat)
client1.receiveData()

