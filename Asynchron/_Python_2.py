import socket
from select import select

# https://www.youtube.com/watch?v=g6xvW2FOuPw&list=PLlWXhlUMyooawilqK4lPXRvxtbYiw34S8&index=2
# .fileno()

# domain:5000

to_monitor = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

# https://serverspace.io/support/help/how-to-install-ncat-tool-on_windows-and-linux/
# ncat -C localhost 5000


def accept_connection(server_sock):
    client_sock, addr = server_socket.accept()
    print('Connection from', addr)

    to_monitor.append(client_sock)


def send_message(client_socket):
    print('Before .recv()')
    try:
        request = client_socket.recv(4096)
        print(request)
        if request:
            response = 'Helloy world\n'.encode()
            client_socket.send(response)
        else:
            client_socket.close()
    except:
        client_socket.close()
        print('Client Outside')


def event_loop():
    while True:

        ready_to_read, _, _ = select(to_monitor, [], [])  # read, write, errors

        for sock in ready_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_message(sock)


if __name__ == '__main__':
    to_monitor.append(server_socket)
    event_loop()
