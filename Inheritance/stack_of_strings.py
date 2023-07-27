class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        if isinstance(element, str):
            self.data.append(element)
        else:
            raise TypeError("Only strings are allowed in the stack.")

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.data.pop()

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        elements = ', '.join(reversed(self.data))
        return f"[{elements}]"