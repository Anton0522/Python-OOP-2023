class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        if isinstance(other, Person):
            new_name = self.name
            new_surname = other.surname
            return Person(new_name, new_surname)
        return NotImplemented


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __repr__(self):
        members = ", ".join([str(person) for person in self.people])
        return f"Group {self.name} with members {members}"

    def __add__(self, other):
        if isinstance(other, Group):
            new_name = f"{self.name} {other.name}"
            new_people = self.people + other.people
            return Group(new_name, new_people)
        return NotImplemented

    def __iter__(self):
        return iter(self.people)
