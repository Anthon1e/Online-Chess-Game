import socket
import pickle
from _thread import *
from board import Board

server = "192.168.0.15"
port = 5555

# setting up a connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind server and port to socket, check if port is being used
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# open up the port, and have multiple clients connect
# blank means unlimited connection
s.listen(2)
print("Waiting for a connection, server started")

players = [Board(True), Board(False)]


def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))    # dump into a pickle object to send
    while True:
        try:
            data = pickle.loads(conn.recv(9000))  # 2048 = amount of bits/information
            if player == 1:
                players[0] = data
            else:
                players[1] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[1]
                else:
                    reply = players[0]
                print("Received: ", data)
                print("Sending: ", reply)

            conn.sendall(pickle.dumps(reply))   # dump into a pickle object to send

        except:
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0

while True:
    # conn = type of object connected, addr = IP Address
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1