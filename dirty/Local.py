import comms.Client

class Local:
    list = dict()
    # Static or Singleton, whatever

    def set(self, name):
        if name not in self.list:  # TODO Do these 2 lines need a mutex?
            self.list[name] = 1

            # TODO Make this sensible, and work
            comms.Client.send('dirty', name)

    def exists(self, name):
        return name in self.list

    def clear(self):
        self.list.clear()
