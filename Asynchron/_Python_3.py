import socket
import selectors

# https://www.youtube.com/watch?v=g6xvW2FOuPw&list=PLlWXhlUMyooawilqK4lPXRvxtbYiw34S8&index=2
# .fileno()

# domain:5000

selector = selectors.DefaultSelector()


def accept_connection(server_socket):
    client_sock, addr = server_socket.accept()
    print('Connection from', addr)

    selector.register(fileobj=client_sock, events=selectors.EVENT_READ, data=send_message)


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)


# https://serverspace.io/support/help/how-to-install-ncat-tool-on_windows-and-linux/
# ncat -C localhost 5000


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
            selector.unregister(client_socket)
    except:
        selector.unregister(client_socket)
        client_socket.close()
        print('Client Outside')


def event_loop():
    while True:
        events = selector.select()  # (key, event)
        # SelectorKey fileobj events data

        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == '__main__':
    server()
    event_loop()
