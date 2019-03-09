from comms import Client


class Remote:
    list_by_folder = dict()
    list_by_peer = dict()

    def set(self, folder, peer):
        # TODO Do we need mutexes over all this stuff? - I think so
        # if name in self.list and self.list[name][peer] != peer:
            # OMGWTFBBQ The dirty flag has failed us.
        if folder not in self.list_by_folder:
            self.list_by_folder[folder] = []
        if peer not in self.list_by_peer:
            self.list_by_peer[peer] = []

        self.list_by_peer[peer].append(folder)
        self.list_by_folder[folder].append(peer)

    def clear_by_folder(self):
        # Loop folders, clear peers with that folder too
        pass

    def clear_by_peer(self):
        # Loop peers, clear folders with that peer too
        pass

    def flush(self, folder):
        for peer in self.list_by_folder[folder]:
            # TODO Make this sensible, and work
            Client.send('flush', folder)
