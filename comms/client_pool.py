"""
Holds a list of Client objects for polling and closure

There are better ways of doing this with select n stuff
"""

import time

class ClientPool:
    pool = []

    def __init__(self):
        pass

    def add(self, client):
        self.pool.append(client)

    def poll(self):
        completed = True
        for client in self.pool:
            if not client.poll():
                completed = False
        return completed

    def wait(self):
        while not self.poll():
            time.sleep(0.01)
