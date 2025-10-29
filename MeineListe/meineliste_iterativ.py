from typing import Any
import time

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
        ergebnis = "["

        schaffner = self._first
        while schaffner is not None:
            ergebnis += repr(schaffner.value)
            if schaffner.next is not None:
                ergebnis += ", "
            schaffner = schaffner.next

        ergebnis += "]"
        return ergebnis

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
        # Generator-Methode, wegen dem yield, bei jedem yield hält die Methode an und liefert den Wert zurück
        wagon = self._first
        while wagon is not None:
            yield wagon.value
            wagon = wagon.next

    def __contains__(self, item):
        # wagon = self._first
        # while wagon is not None:
        #     if wagon.value == item:
        #         return True
        #     wagon = wagon.next
        # return False
        for elem in self:
            if elem == item:
                return True
        return False



    def append(self, value: Any) -> None:
        if self._first is None:
            self._first = self._Wagon(value)
        else:
            schaffner = self._first
            while schaffner.next is not None:
                schaffner = schaffner.next
            schaffner.next = self._Wagon(value)

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

    def unique1(self):
        '''unique mit neuer Liste'''
        u_liste = Liste()
        schaffner_original = self._first
        while schaffner_original is not None:
            vorhanden = False
            schaffner_u_liste = u_liste._first
            while schaffner_u_liste is not None:
                if schaffner_u_liste.value == schaffner_original.value:
                    vorhanden = True
                    break
                else:
                    schaffner_u_liste = schaffner_u_liste.next
            if not vorhanden:
                u_liste.append(schaffner_original.value)

            schaffner_original = schaffner_original.next

        return u_liste

    def unique2(self):
        '''unique mit Änderung im Original'''
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
        return

    def bubble_sort(self):
        laenge = len(self)
        swapped = True
        while swapped:
            swapped = False
            for i in range(laenge - 1):
                if self[i] > self[i + 1]:
                    self[i], self[i + 1] = self[i + 1], self[i]
                    swapped = True
                if i == laenge-1:
                    laenge -= 1





