'''
Meine rekusive Liste
'''
from typing import Any


class Liste:
    class _Wagon:
        def __init__(self, value: Any):
            self.next = None
            self.value = value

        def __repr__(self):
            if self.next is None:
                return f'{repr(self.value)}'
            else:
                return f'{repr(self.value)}, {repr(self.next)}'

        def __len__(self):
            if self.next is None:
                return 1
            return len(self.next) + 1

        def append(self, value: Any):
            if self.next is None:
                self.next = Liste._Wagon(value)
            else:
                self.next.append(value)

        def copy(self):
            wagon_kopie = Liste._Wagon(self.value)
            if self.next is not None:
                wagon_kopie.next = self.next.copy()
            return wagon_kopie

        def __getitem__(self, index: int):
            if index == 0:
                return self.value
            return self.next.__getitem__(index-1)
    class _Iterator:
        def __init__(self, first: Any):
            self.temp = first

        def __next__(self) -> Any:
            if self.temp is not None:
                v = self.temp.value
                self.temp = self.temp.next
                return v
            raise StopIteration

    def __init__(self):
        self._first = None

    def __repr__(self):
        if self._first is None:
            return '[]'
        else:
            return f'[{self._first}]'

    def __len__(self):
        if self._first is None:
            return 0
        return len(self._first)

    def append(self, value: Any):
        if self._first is None:
            self._first = self._Wagon(value)
        else:
            self._first.append(value)

    def copy(self):
        kopie = Liste()
        if self._first is not None:
            kopie._first = self._first.copy()
        return kopie

    def __getitem__(self, index: int):
        if self._first is None or index < 0 or index >= len(self):
            raise IndexError("list index out of range")
        if type(index) is not int:
            raise TypeError("index must be integer")
        return self._first.__getitem__(index)

    def __iter__(self):
        return self._Iterator(self._first)





