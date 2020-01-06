import pickle


class Museum:

    def __init__(self, name):
        self.name = name

    @classmethod
    def from_file(cls, filename):
        return pickle.load(filename)

    def save(self):

    def filename
