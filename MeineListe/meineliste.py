from typing import Any


class Liste:
    def __init__(self):
        self.first = None

    def __str__(self):
        return "[]"

    def append(self, value:Any) -> None:
        if self.first is None:
            self.first = Wagon(value)
        else:
            schaffner = self.first
            while schaffner.next is not None:
                schaffner = schaffner.next
            schaffner.next = Wagon(value)

    def __len__(self) -> int:
        if self.first is None:
            return 0
        else:
            schaffner = self.first
            counter = 1
            while schaffner.next is not None:
                counter += 1
            return counter

class Wagon:
    def __init__(self, value):
        self.next = None
        self.value = value


