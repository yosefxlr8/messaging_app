import socket

# Buying a phone and choosing it's type precisely for the need
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Insert the Sim card (bind the phone into a phone number)
server_socket.bind((socket.gethostname(), 1234))

# listening or waiting for someone to call me
server_socket.listen(5)

# accepting the call and send some information
# and then close the phone call and wait for another and repeat
while True:
    client_socket, address = server_socket.accept()
    print(client_socket.recv(10024).decode('utf-8'))
    msg ='Hello Josh How are you today?'.encode('UTF-8')
    client_socket.send(msg)
    client_socket.close()


