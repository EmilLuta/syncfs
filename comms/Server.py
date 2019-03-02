"""
TODO This was copied from https://docs.python.org/3.5/library/socketserver.html#module-socketserver
TODO and needs to be tidied up...
"""

import socket
import threading
import socketserver

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        cur_thread = threading.current_thread()
        response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
        self.request.sendall(response)
        """
        TODO Something like:
            if data === "get-dirty":
                self.request.sendall(get_dirty_list_from_somewhere())
        """

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class Server:
    server = None

    def __init__(self):
        HOST, PORT = "localhost", 0

        self.server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
        ip, port = self.server.server_address

        # Start a thread with the server -- that thread will then start one more thread for each request
        server_thread = threading.Thread(target=self.server.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()

    def __del__(self):
        self.server.shutdown()
        self.server.server_close()



