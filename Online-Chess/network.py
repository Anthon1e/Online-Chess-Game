import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.15"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        # When we connect, we send validation token back to a client
        # self.p will have 'Connected'
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))  # decompose objects' data / load bytes data
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))    # dump into a pickle object to send
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)
