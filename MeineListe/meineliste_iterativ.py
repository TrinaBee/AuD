from typing import Any


class Liste:
    class _Wagon:
        def __init__(self, value):
            self.next = None
            self.value = value

        def __repr__(self):
            if self.next is None:
                return f'{repr(self.value)}'
            else:
                return f'{repr(self.value)}, {repr(self.next)}'

        def __len__(self) -> int:
            if self.next is None:
                return 1
            else:
                return len(self.next) + 1

    def __init__(self):
        self._first = None

    def __str__(self):
        if self._first is None:
            return "[]"
        ergebnis = repr(self._first)
        schaffner = self._first
        while schaffner.next is not None:
            schaffner = schaffner.next
            ergebnis += f", {repr(schaffner)}"
        return f"[{ergebnis}]"

    def append(self, value: Any) -> None:
        if self._first is None:
            self._first = self._Wagon(value)
        else:
            schaffner = self._first
            while schaffner.next is not None:
                schaffner = schaffner.next
            schaffner.next = self._Wagon(value)

    def __len__(self) -> int:
        if self._first is None:
            return 0
        else:
            schaffner = self._first
            counter = 1
            while schaffner.next is not None:
                schaffner = schaffner.next
                counter += 1
            return counter



