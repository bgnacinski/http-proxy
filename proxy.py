import socket

def handle_client(client):
    data = client.recv(131072)
    buffer = data

    website_address = str(buffer).split()[3].split("\\")[0]

    print(website_address)

    websocket = socket.socket()
    websocket.connect((website_address, 80))
    websocket.send(buffer)

    resp = websocket.recv(40000)

    return resp

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 1025))
s.listen(1024)

connections = 0

print("Server hosted")

while True:
    client, addr = s.accept()

    print("Connection established with " + addr[0])
    print(connections)

    client.send(handle_client(client))

    client.close()
    print("Connection closed")
