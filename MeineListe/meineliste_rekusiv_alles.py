from typing import Any


class Liste:
    def __init__(self):
        self.first = None

    def __str__(self):
        return '[]'


    # def append(self, value: Any) -> None:#rekusives hinzufügen nur Lok
    #     # if self.first is None:
    #     #     self.first = Wagon(value)
    #     # else:
    #     #     schaffner = self.first
    #     #     while schaffner.next is not None:
    #     #         schaffner = schaffner.next
    #     #     schaffner.next = Wagon(value)
    #     def append_rekusiv(wagon:Wagon):
    #         if wagon.next is None:
    #             wagon.next = neuer_wagon
    #         else:
    #             append_rekusiv(wagon.next)
    #     neuer_wagon = Wagon(value)
    #     if self.first is None:
    #         self.first = neuer_wagon
    #     else:
    #         append_rekusiv(self.first)

    def append(self, wagon:Any): #reksuives hinzufügen über die Wagons

        if self.first is None:
            self.first = Wagon(wagon)
        else:
            self.first.append(wagon)

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
        return len(self.first)


class Wagon:
    def __init__(self, value):
        self.next = None
        self.value = value

    # def __len__(self) -> int: # Rückweg
    #     if self.next is None:
    #         return 1
    #     else:
    #         return len(self.next) + 1

    def __len__(self) -> int: # Vorwärts
      def len_wagon_rekusiv(wagon:Wagon, counter):
          if wagon.next is None:
              return counter + 1
          else:
              return len_wagon_rekusiv(wagon.next, counter + 1)
      if self.next is None:
          return 1
      else:
          return len_wagon_rekusiv(self.next, 1)

    def append(self, neuer_wagon:'Wagon'):

        if self.next is None:
            self.next = neuer_wagon
        else:
            self.next.append(neuer_wagon)
