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

    def __str__(self):
        if self._first is None:
            return "[]"
        ergebnis = "["

        schaffner = self._first
        while schaffner is not None:
            ergebnis += repr(schaffner.value)
            if schaffner.next is not None:
                ergebnis += ", "
            schaffner = schaffner.next

        ergebnis += "]"
        return ergebnis


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

    def copy(self):
        kopie = Liste()
        if self._first is None:
            return kopie
        else:
            schaffner = self._first
            kopie.append(schaffner.value)
            while schaffner.next is not None:
                schaffner = schaffner.next
                kopie.append(schaffner.value)
            return kopie

    def __getitem__(self, index: int):
        if self._first is None or index < 0:
            raise IndexError("list index out of range")
        if type(index) is not int:
            raise TypeError("index must be integer")
        schaffner = self._first
        counter = 0
        while schaffner is not None:
            if index == counter:
                return schaffner.value
            schaffner = schaffner.next
            counter += 1
        raise IndexError("list index out of range")

    def __iter__(self):
        return self._Iterator(self._first)

    def unique1(self):
        u_liste = Liste()
        schaffner_original = self._first
        while schaffner_original is not None:   #Schaffner rennt durch die orignale Liste
            vorhanden = False
            schaffner_u_liste = u_liste._first
            while schaffner_u_liste is not None:    #Schaffner unique Liste rennt so lange durch die neue Liste bis er durch die neue Liste
                if schaffner_u_liste.value == schaffner_original.value: #vergleicht die values
                    vorhanden = True
                    break
                else:
                    schaffner_u_liste = schaffner_u_liste.next
            if vorhanden is False:
                u_liste.append(schaffner_original.value)

            schaffner_original = schaffner_original.next

        return u_liste


    def unique2(self):
        schaffner = self._first

        while schaffner is not None:
            vorgaenger = schaffner
            kontroletti = schaffner.next
            while kontroletti is not None:
                nachfolger = kontroletti.next
                if kontroletti.value == schaffner.value:
                    vorgaenger.next = nachfolger
                else:
                    vorgaenger = kontroletti
                kontroletti = nachfolger
            schaffner = schaffner.next
        return self





