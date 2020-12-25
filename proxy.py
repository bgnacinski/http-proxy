import client as client_handler
import threading
import datetime
import socket
import json

def update_log(address):
    global LOG_FILE

    now = datetime.datetime.now()

    hour = now.hour
    minute = now.minute
    second = now.second

    year = now.year
    month = now.month
    day = now.day

    data_to_write = f"[{day}.{month}.{year} - {hour}:{minute}:{second}] {address}"

    f = open(LOG_FILE, "a")
    f.write(data_to_write)
    f.close()

# Getting config
config = json.load(open("config.json"))

PUBLIC_ADDR = config["public_address"]
PORT = config["port"]
MAX_CONNECTIONS = config["max_connections"]
LOG_FILE = config["log_dir"]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((PUBLIC_ADDR, PORT))
s.listen(MAX_CONNECTIONS)

print("Server hosted")

while True:
    client, addr = s.accept()

    update_log(addr[0])

    client_thread = threading.Thread(target=client_handler.handle_http, args=(client,))
    client_thread.start()