import client as client_handler
import threading
import datetime
import socket

def update_log(address):
    now = datetime.datetime.now()

    hour = now.hour
    minute = now.minute
    second = now.second

    year = now.year
    month = now.month
    day = now.day

    data_to_write = f"[{day}.{month}.{year} - {hour}:{minute}:{second}] {address}"

    f = open("access.log", "a")
    f.write(data_to_write)
    f.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 1025))
s.listen(1024)

print("Server hosted")

while True:
    client, addr = s.accept()

    update_log(addr[0])

    client_thread = threading.Thread(target=client_handler.handle, args=(client,))
    client_thread.start()