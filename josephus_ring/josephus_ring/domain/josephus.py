class JosephusRing:
    def __init__(self, start = 1, step = 1):
        if start < 1:
            self.start = 1
        else:
            self.start = start
        if step < 1:
            self.step = 1
        else:
            self.step = step            

        self.people = []

    def append(self, obj):
        self.people.append(obj)

    def pop(self, index = None):
        if not index:
            self.people.pop()
        else:
            self.people.pop(index)

    def query_list(self):
        ret = []
        temp = self.people[:]
        size = len(temp)
        if size == 0:
            return ret

        current_index = self.start - 1
        for _ in range(size):
            current_index = (current_index + self.step - 1) % len(temp)
            obj = temp.pop(current_index)
            ret.append(obj)
        return ret

    def __iter__(self):
        return self

    def __next__(self):
        if not self.people:
            raise StopIteration

        current_index = self.start - 1
        index = (current_index + self.step - 1) % len(self.people)
        self.start = index + 1
        obj = self.people.pop(index)
        return obj