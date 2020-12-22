import socket

def handle(client:socket.socket):
    http_request = client.recv(131072) # default apache2 BufferSize

    website_address = str(http_request).split()[3].split("\\")[0]

    #getting content of site
    websocket = socket.socket()
    websocket.connect((website_address, 80))
    websocket.send(http_request)

    while True:
        chunk = websocket.recv(8192) # default apache2 ChunkSize

        #dynamically sending chunks
        client.send(chunk)

    client.close()

def get_domain_name(request:bytes):
    domain_name = str(request).split()[3].split("\\")[0]

    return domain_name