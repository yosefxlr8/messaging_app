import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((socket.gethostname(), 1234))

while True:
    data = my_socket.recv(1024)
    print(data.decode('utf-8'), end='')
    msg = input('\nYou: ')
    if msg == '__done__':
        break
    my_socket.send(msg.encode('utf-8'))
my_socket.close()
print('done')