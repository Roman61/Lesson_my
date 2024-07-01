import socket

# domain:5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

# https://serverspace.io/support/help/how-to-install-ncat-tool-on_windows-and-linux/
# ncat -C localhost 5000

while True:
    print("Before .accept()")
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)

    while True:
        print('Before .recv()')
        try:
            request = client_socket.recv(4096)
            print(request)

            if not request:
                break
            else:
                response = 'Helloy world\n'.encode()
                client_socket.send(response)
        except:
            client_socket.close()
            print('Client Outside')
            break

    print('Outside inner while loop')
    client_socket.close()
