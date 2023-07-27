class vowels:
    def __init__(self, text):
        self.text = text
        self.vowels = ['a', 'i', 'o', 'u', 'y',"e"]
        self.current_idx = -1
        self.end_idx = len(text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_idx += 1
        if self.current_idx > self.end_idx:
            raise StopIteration()

        current_element = self.text[self.current_idx]
        if current_element.lower() in self.vowels:
            return current_element

        return self.__next__()
