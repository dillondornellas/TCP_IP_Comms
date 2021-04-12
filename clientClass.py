import socket
import time
import sys 

class tcpClient:
    def __init__(self):
        self.local_hostname = socket.gethostname()
        self.ip_address = socket.gethostbyname(self.local_hostname)
        self.port = 10000
        self.initConnection()
        # create containers for param codes
        self.m11 = []
        self.m22 = []
        self.m33 = []
        # storage for incomplete message
        self.holder = ''

    def initConnection(self):  
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (self.ip_address, self.port)
        try:
            # connect to the server
            self.client.connect(server_address)
            print (sys.stderr, "connecting to %s with %s" % (self.local_hostname, self.ip_address))
        except:
            print (sys.stderr, "Unable to connect to server at %s" % (self.ip_address))

    def sendData(self, data):
        try:
            # send data to the server
            self.client.send(bytes(data,'ascii'))
            print(sys.stderr, "sending data to server at %s" % self.ip_address)
        except:
            print(sys.stderr, 'unable to connect to server')

    def receiveData(self):
        while True:
            try:
                # receive data from the server
                data = self.client.recv(1024).decode('ascii')
                print(sys.stderr, 'received: \n %s' % data)
                # send decoded data to dataHandler for processing
                self.dataHandler(data)
                break
            except:
                print(sys.stderr, 'echo not received from server')
                break

    def packageData(self, data):
        # concatinate the string data between STX prefix ("/x02") and ETX suffix ("/x03")
        new_data = '/x02' + data + '/x03'
        return new_data

    def dataHandler(self, data):
        print('******DATA BEING HANDLED******')

        # check if there is an incomplete message from last received data packet
        if self.holder != '':
            # concatinate the incomplete message to the beggining of the new data packet
            data = self.holder + data
            # clear the holder
            self.holder = ''

        # separate data messages into individual strings
        dataList = data.split('\x00')

        # remove any empty strings caused by the last split opperation
        try:
            dataList.remove('')
        except:
            pass

        # check if the last message of the data is complete (all messages should contain two ']' characters)
        if dataList[-1].count(']') != 2:
            # remove and store the incomplete element from the data packet 
            self.holder = dataList.pop()
            print('incomplete message, storing for next packet reception \'%s\'' % self.holder )
        else:
            print('no incomplete messages in packet')

        # cycling through each message for string processing
        for element in dataList:
            # extract the [param_code]
            param_code = element.split('[', 1)[1].split(']')[0]
            # extract the message and convert to a list
            msg = element.split('][')[1].split(']')[0].split(',')
            # convert the message values to floats
            msg_float = [float(i) for i in msg]

            # append the message contents to its corresponding attribute variable
            if   param_code == '11':
                self.m11.append(msg_float)
            elif param_code == '22':
                self.m22.append(msg_float)
            elif param_code == '33':
                self.m33.append(msg_float)
        print('***********COMPLETE***********')



# PROVIDED DATA
dat1 = '[11][0.6687949706053933, 0.9866176447505118, 0.3482928666204528]\x00[22][9, -16, -28]\x00[33][1, 1, 1]\x00[11][0.882335774796032, 0.33114033843835633, 0.1579493784169541]\x00[22][-4, -18, -17]\x00[33][0, 0, 0]\x00[11][0.3433161171529475, 0.23603251725235308, 0.49143138904346184]\x00[22][4, 17, -30]\x00[33][1, 0, 1]\x00[11][0.33408755020101877, 0.23387336003172676, 0.9174727724578773]\x00[22][8, -4, -11]\x00[33][0, 0, 1]\x00[11][0.41577553052979666, 0.47894390322286884, 0.7338557598861271]\x00[22][6, 15, 3]\x00[33][0, 0, 0]\x00[11][0.17856591909478592, 0.6400568604819764, 0.3958512065334282]\x00[22][-9, -13, -11]\x00[33][0, 1, 1]\x00[11][0.813781998790508, 0.37802430505925766, 0.424373807370117]\x00[22][5, -6, -21]\x00[33][0, 1, 0]\x00[11][0.8992240626200263, 0.20096023406062724, 0.4298957057137537]\x00[22][0, -4, 3]\x00[33][0, 0, 1]\x00[11][0.3393822880909392, 0.28125673261356143, 0.43181603402861146]\x00[22][-5, 2, -21]\x00[33][0, 0, 0]\x00[11][0.9357641322644188, 0.6131036709069413, 0.9235705177483603]\x00[22][-9, -14, 13]\x00[33][1, 1, 1]\x00'
dat2 = '[11][0.813781998790508, 0.37802430505925766, 0.424373807370117]\x00[22][5, -6, -21]\x00[33][0, 1, 0]\x00[11][0.8992240626200263, 0.20096023406062724, 0.4298957057137537]\x00[22][0, -4, 3]\x00[33][0, 0, 1]\x00[11][0.3393822880909392, 0.28125673261356143, 0.43181603402861146]\x00[22][-5, 2, -21]\x00[33][0, 0,0]\x00[11][0.9357641322644188, 0.6131036709069413, 0.9235705177483603]\x00[22][-9, -14, 13]\x00[33][1, 1, 1]\x00[11][0.8538425091197278, 0.517496999362361, 0.4831133'
dat3 = '63107483]\x00[22][7, -11, 21]\x00[33][0, 0, 1]\x00[11][0.4836867569220712, 0.352088035849766, 0.048481221620155]\x00[22][-5, -19, 23]\x00[33][0, 1, 1]\x00[11][0.9306009710144248, 0.3629941965090451, 0.8623470468607274]\x00[22][7, -5, -25]\x00[33][1, 1, 0]\x00[11][0.5145808711857979, 0.03436334200766278, 0.6239658521602299]\x00[22][-2, 11, 25]\x00[33][0, 0, 0]\x00[11][0.7859663758828682, 0.7866047825713807, 0.4652918403180918]\x00[22][-1, 17, 13]\x00[33][1, 1, 1]\x00[11]'

# create instance of client class
client1 = tcpClient()

# send first data packet
client1.sendData(dat1)
time.sleep(1)
client1.receiveData()

# send second data packet
client1.sendData(dat2)
time.sleep(1)
client1.receiveData()

# send third data packet
client1.sendData(dat3)
time.sleep(1)
client1.receiveData()

# printing results
print('Param code results: ')
print("m11 result:")
for res in client1.m11:
    print(res)
print("m22 result:")
for res in client1.m22:
    print(res)
print("m33 result:")
for res in client1.m33:
    print(res)

