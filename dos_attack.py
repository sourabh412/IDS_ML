import socket
import time
from utils import *

attack_time = 10

# socket creation
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connection
server_addr = ('localhost', 10000)
client.connect(server_addr)
print("Connection estabished\n")

start_time = end_time = time.time()

while end_time - start_time < Attack_time:
    end_time = time.time()
    time.sleep(0.05)
    print(MSG)
    client.send(MSG.encode())

client.send("attack".encode())

client.close()