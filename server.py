import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 1234))

server_socket.listen(5)

while True:
    socket1, address1 = server_socket.accept()
    print(f'Established connection with {address1}')
    socket1.send('Send a message'.encode('utf-8'))

    socket2, address2 = server_socket.accept()
    print(f'Established connection with {address1}')

    while True:
        msg = socket1.recv(1024)
        socket2.send(msg)

        msg = socket2.recv(1024)
        socket1.send(msg)

    socket1.close()
    socket2.close()

