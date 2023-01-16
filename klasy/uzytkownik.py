class uzytkownik:
    def __init__(self,nazwa,hasło,karta,pracownik):
        self.nazwa = nazwa
        self.hasło = hasło
        self.karta = karta
        self.pracownik = pracownik
    
    def pself(self):
        print(self.nazwa)
        qq = int(input("""
        Czy chcesz zedytować?
        1 = Tak
        2 = Nie
        """))
        if qq == 1:
            self.nazwa = input("Nowa nazwa:")
        if qq == 2:
            print("Nie wprowadzam zmian")
        else:
            pass

    def phaslo(self):
        print(self.hasło)
        qq = int(input("""
        Czy chcesz zedytować?
        1 = Tak
        2 = Nie
        """))
        if qq == 1:
            self.hasło = input("Nowe hasło:")
        if qq == 2:
            print("Nie wprowadzam zmian")
        else:
            pass

    def pkarta(self):
        print(self.karta)
        qq = int(input("""
        Czy chcesz zedytować?
        1 = Tak
        2 = Nie
        """))
        if qq == 1:
            self.karta = int(input("Nowy numer karty:"))
        if qq == 2:
            print("Nie wprowadzam zmian")
        else:
            pass

    def pokapracownik(self):
        print(self.pracownik)
        qq = int(input("""
         Czy chcesz zedytować?
        1 = Tak
        2 = Nie
        """))
        if qq == 1:
            qqq = int(input("""
            pracownik biurowy = 1
            inny (np techniczny) = 2
            """))
            if qqq == 1:
                self.pracownik = True
            if qqq == 2:
                self.pracownik = False
        if qq == 2:
            print("Nie wprowadzam zmian")
        else:
            pass
