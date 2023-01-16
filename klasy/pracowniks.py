from pracownikb import pracownikb
class pracowniks(pracownikb):
    def __init__(self, zarobki, autos, lodzialow, lata):
        self.zarobki = zarobki
        self.autos = autos
        self.lodzialow = lodzialow
        self.lata = lata

    def poddzial(self):
        print(self.zarobki)
        qq = int(input("""
        Czy chcesz zedytować
        1 = tak
        2 = nie
        """))
        if qq == 1:
            self.zarobki = input("Nowe zarobki:")
        elif qq == 2:
            ("Nie wprowadzam zmian.")
        else:
            pass

    def pautos(self):
        print(self.autos)
        qq = int(input("""
        Czy chcesz zedytować
        1 = tak
        2 = nie
        """))
        if qq == 1:
            self.autos = input("Nowe auto::")
        elif qq == 2:
            ("Nie wprowadzam zmian.")
        else:
            pass

    def poddzial(self):
        print(self.lodzialow)
        qq = int(input("""
        Czy chcesz zedytować
        1 = tak
        2 = nie
        """))
        if qq == 1:
            self.skarga = int(input("Nowa liczba odzialow:"))
        elif qq == 2:
            ("Nie wprowadzam zmian.")
        else:
            pass

    def plat(self):
        print(self.lata)
        qq = int(input("""
        Czy chcesz zedytować
        1 = tak
        2 = nie
        """))
        if qq == 1:
            self.lata = int(input("Nowa liczba lat do emerytury"))
        elif qq == 2:
            ("Nie wprowadzam zmian.")
        else:
            pass