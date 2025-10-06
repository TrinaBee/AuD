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



