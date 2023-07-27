class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current = 0
        self.iteration = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration >= self.count:
            raise StopIteration
        result = self.current
        self.current += self.step
        self.iteration += 1
        return result
