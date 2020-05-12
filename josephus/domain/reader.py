class Reader:
    def __iter__(self):
        raise NotImplementedError

    def __next__(self):
        raise NotImplementedError