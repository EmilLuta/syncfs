from comms import Client


class Local:
    changes = dict()
    # Static or Singleton, whatever

    def set(self, name):
        if name not in self.changes:  # TODO Do these 2 lines need a mutex? - Pretty much
            self.changes[name] = 1

            # TODO Make this sensible, and work
            Client.send('dirty', name)

    def exists(self, name):
        return name in self.changes

    def clear(self):
        self.changes.clear()  # I think self.changes = {} is more space time efficient
