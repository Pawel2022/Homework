from silnik import Silnik
from akumulator import Akumulator

class Auto:
    def __init__(self, wlasciciel : str) -> None:
        self.__wlascicel = wlasciciel
        self.__akumlator = Akumulator()
        self.__silnik = Silnik()

    def all_information(self):
        print("="*40)
        print(self.__wlascicel)
        self.__akumlator.informacje()
        self.__silnik.informacje()
        print("="*40)

    def zmien_informacje(self):
        print("co chcesz zmienic")
        print("a - silnik")
        print("b - akumulator")
        inp = input().lower().strip()
        if inp == "a":
            self.__silnik.zmien_informacje_silnik()
        elif inp == "b":
            self.__akumlator.zmien_dane_akumolatora()

    def brrrbrrrr(self):
        self.__silnik.brrrbrrrr()
        