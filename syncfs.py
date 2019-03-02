#!/usr/bin/env python

import logging
import os

from errno import EACCES
from os.path import realpath
from threading import Lock

from fuse import FUSE, FuseOSError, Operations, LoggingMixIn

import filesystem.Fuse
import comms.Server
import comms.Client
import comms.ClientPool

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('root')
    parser.add_argument('mount')
    args = parser.parse_args()

    server = comms.Server()
    peers = find_peers() # TODO This should exist :)
    pool = comms.ClientPool()
    for peer in peers:
        pool.add(comms.Client(peer[id], 'register', 'filesystem name/ID'))
        pool.wait();

    logging.basicConfig(level=logging.DEBUG)
    fuse = FUSE(
        Loopback(args.root), args.mount, foreground=True, allow_other=True)
    print('FUSE shutdown')

    client = comms.Client('deregister')
    client.response()

    del server
    print('Server shutdown')