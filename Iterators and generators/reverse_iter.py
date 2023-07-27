class reverse_iter:
    def __init__(self,collection):
        self.collection = collection
        self.start_index = len(self.collection) - 1
        self.end_index = 0
        self.current = self.start_index + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current -= 1
        if self.current < self.end_index:
            raise StopIteration()
        return self.collection[self.current]
