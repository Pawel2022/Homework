from uzytkownik import uzytkownik
class podopieczny(uzytkownik):
    def __init__(self, ddo, cs, wiek, spec):
        self.ddo = ddo
        self.cs = cs
        self.wiek = wiek
        self.spec = spec

    def pddo(self):
        print(self.ddo)
        qq = int(input("""
        Czy chcesz zedytować?
        1 = Tak
        2 = Nie
        """))
        if qq == 1:
            self.ddo = input("Do jakich oddzialow ma dostep:")
        if qq == 2:
            print("Nie wprowadzam zmian")
        else:
            pass

    def pcs(self):
        print(self.cs)
        qq = int(input("""
        Czy chcesz zedytować?
        1 = Tak
        2 = Nie
        """))
        if qq == 1:
            self.cs = input("Nowy czas pracy:")
        if qq == 2:
            print("Nie wprowadzam zmian")
        else:
            pass

    def pcs(self):
        print(self.wiek)
        qq = int(input("""
        Czy chcesz zedytować?
        1 = Tak
        2 = Nie
        """))
        if qq == 1:
            self.wiek = int(input("Nowy wiek:"))
        if qq == 2:
            print("Nie wprowadzam zmian")
        else:
            pass

    def pspec(self):
        print(self.spec)
        qq = int(input("""
        Czy chcesz zedytować?
        1 = Tak
        2 = Nie
        """))
        if qq == 1:
            self.cs = input("Nowa specjalizacja:")
        if qq == 2:
            print("Nie wprowadzam zmian")
        else:
            pass