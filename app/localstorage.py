import shelve

class LocalStorage():
    def __init__(self):
        self.shelf = shelve.open('storage/sessions/session')

    def close(self):
        self.shelf.close()

    def save(self):
        self.shelf.sync()