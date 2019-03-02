"""
Connects to a peer via TCP/IP to send/receive peer lists, transactions, dirty flags etc
"""

import time

class Client:
    def __init__(self, name, payload, response_cb):
        # Do the TCP/IP call here
        pass

    def poll(self):
        # Checks the socket is still open, used by ClientPool n stuff
        pass

    def response(self):
        while not self.poll():
            time.sleep(0.01)

"""
Example from socketserver:

def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        print("Received: {}".format(response))
"""
