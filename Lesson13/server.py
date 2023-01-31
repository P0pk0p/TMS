import socket

serv_sock = socket.socket(socket.AF_INET,
                          socket.SOCK_STREAM)
serv_sock.bind(('127.0.0.1', 55234))
serv_sock.listen(1)
print('server started')
client_sock, client_addr = serv_sock.accept()
print(f'accept connection: {client_addr}')

while True:
    data = client_sock.recv(1024)

    if not data:
        break

    data = data.decode('utf-8')
    if data == 'greeting':
        response = 'Hello'
    else:
        response = data
    client_sock.sendall(response.encode('utf-8'))

serv_sock.close()