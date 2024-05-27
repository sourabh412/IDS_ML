import socket
import pickle
from utils import *

# socket creation
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ("localhost", 10000)

# bind
server.bind(server_addr)

# listen
server.listen(1)

model = pickle.load(open(Model_path, "rb"))

# accept
conn, client_addr = server.accept()

# print(conn.recv(1028).decode())

while Label != "attack":
    data = conn.recv(1028).decode()
    label = Model.predict(Data)
    Label = data

print("System under attack ...")

# end
print("Closing connection")
conn.close()
server.close()