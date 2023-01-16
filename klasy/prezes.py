from pracowniks import pracowniks
class prezes(pracowniks):
    def __init__(self, dochod, liczbap, kary, glklijent):
        self.dochod = dochod
        self.liczbap = liczbap
        self.kary = kary
        self.glklijent = glklijent

    def pdochod(self):
        print(self.dochod)
        qq = int(input("""
        Czy chcesz zedytować?
        1 = Tak
        2 = Nie
        """))
        if qq == 1:
            self.dochod = int(input("Nowy dochod"))
        if qq == 2:
            print("Nie wprowadzam zmian")
        else:
            pass

    def pliczbap(self):
        print(self.liczbap)
        qq = int(input("""
        Czy chcesz zedytować?
        1 = Tak
        2 = Nie
        """))
        if qq == 1:
            self.dochod = int(input("Nowa liczba pracownikow"))
        if qq == 2:
            print("Nie wprowadzam zmian")
        else:
            pass

    def pkary(self):
        print(self.dochod)
        qq = int(input("""
        Czy chcesz zedytować?
        1 = Tak
        2 = Nie
        """))
        if qq == 1:
            self.dochod = int(input("Nowa liczba kar:"))
        if qq == 2:
            print("Nie wprowadzam zmian")
        else:
            pass

    def pglklijent(self):
        print(self.glklijent)
        qq = int(input("""
        Czy chcesz zedytować?
        1 = Tak
        2 = Nie
        """))
        if qq == 1:
            self.glklijent = input("Nowy glowny klijent:")
        if qq == 2:
            print("Nie wprowadzam zmian")
        else:
            pass