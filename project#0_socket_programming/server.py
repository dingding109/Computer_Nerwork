import socket

HOST = '192.168.0.23'

PORT = 8000

BUFFER = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((HOST, PORT))

sock.listen(0)

print('tcpServer listen at: %s:%s\n\r' % (HOST, PORT))

while True:
    client_sock, client_addr = sock.accept()
    print('%s:%s connect' % client_addr)

    while True:

        recv = client_sock.recv(BUFFER)

        if not recv:
            client_sock.close()

            break

        print('[Client %s:%s said]:%s' % (client_addr[0], client_addr[1], recv))

        client_sock.send('tcpServer has received your message'.encode())

sock.close()
