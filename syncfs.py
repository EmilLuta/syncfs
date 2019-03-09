#!/usr/bin/env python

import logging
import argparse

from fuse import FUSE

from comms import Server
from comms import Client
from comms import ClientPool

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('root')
    parser.add_argument('mount')
    args = parser.parse_args()

    server = Server()
    peers = find_peers()  # TODO This should exist :)
    pool = ClientPool() # you could initialize pool with peers,
    # instead of doing this here. Like ClientPool(peers)
    for peer in peers:
        pool.add(Client(peer[id], 'register', 'filesystem name/ID'))
        pool.wait()

    logging.basicConfig(level=logging.DEBUG)
    fuse = FUSE(
        Loopback(args.root), args.mount, foreground=True, allow_other=True)
    print('FUSE shutdown')

    client = Client('deregister')
    client.response()

    del server # Not sure what you expect this line to do
    # The garbage collector will collect it anyways.
    # If you want to close the connections,
    # one usually writes either a close method that you can call or
    # make server a context manager that knows how to close itself
    print('Server shutdown')
