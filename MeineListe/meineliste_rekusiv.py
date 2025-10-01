from typing import Any


class Liste:
    def __init__(self):
        self.first = None

    def __str__(self):
        return "[]"

    def append(self, value: Any) -> None:
        if self.first is None:
            self.first = Wagon(value)
        else:
            schaffner = self.first
            while schaffner.next is not None:
                schaffner = schaffner.next
            schaffner.next = Wagon(value)

    # def __len__(self) -> int: #rekusiv - Rückweg
    #     def len_rekursiv(wagon: Wagon) -> int:
    #         if wagon.next is None:
    #             return 1
    #         return len_rekursiv(wagon.next) + 1
    #
    #     if self.first is None:
    #         return 0
    #     return len_rekursiv(self.first)

    # def __len__(self) -> int: #rekusiv - Hinweg
    #     def len_rekursiv(wagon: Wagon, counter) -> int:
    #         if wagon.next is None:
    #             return counter + 1
    #         else:
    #             return len_rekursiv(wagon.next, counter + 1)
    #
    #     if self.first is None:
    #         return 0
    #     return len_rekursiv(self.first, 0)

    # def __len__(self) -> int:  # rekusiv - Mit len von Klasse Wagon Rückweg
    #     if self.first is None:
    #         return 0
    #     return len(self.first)

    def __len__(self) -> int:  # rekusiv - Mit len von Klasse Wagon Hinweg
        if self.first is None:
            return 0
        return len(self.first,0)


class Wagon:
    def __init__(self, value):
        self.next = None
        self.value = value

    # def __len__(self) -> int: # Rückweg
    #     if self.next is None:
    #         return 1
    #     else:
    #         return len(self.next) + 1

    def __len__(self, counter) -> int: # Vorwärts
        if self.next is None:
            return counter
        else:
            return len(self.next(counter + 1))
