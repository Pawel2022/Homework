from uzytkownik import uzytkownik
class pracownikinny(uzytkownik):
    def __init__(self,skargi,wolne,stanowisko,kontaktk):
        self.skargi = skargi
        self.wolne = wolne
        self.stanowisko = stanowisko
        self.kontaktk = kontaktk

    def pskarga(self):
        print(self.skarga)
        qq = int(input("""
        Czy chcesz zedytować
        1 = tak
        2 = nie
        """))
        if qq == 1:
            self.skarga = input("Nowa skarga")
        elif qq == 2:
            ("Nie wprowadzam zmian.")
        else:
            pass

    def pwolne(self):
        print(self.wolne)
        qq = int(input("""
        Czy chcesz zedytować
        1 = tak
        2 = nie
        """))
        if qq == 1:
            self.skarga = input("Nowe wolne")
        elif qq == 2:
            ("Nie wprowadzam zmian.")
        else:
            pass

    def pstanowisko(self):
        print(self.stanowisko)
        qq = int(input("""
        Czy chcesz zedytować
        1 = tak
        2 = nie
        """))
        if qq == 1:
            self.stanowisko = input("Stanowisko:")
        elif qq == 2:
            ("Nie wprowadzam zmian.")
        else:
            pass

    def pkontaktk(self):
        print(self.kontaktk)
        qq = int(input("""
        Czy chcesz zedytować
        1 = tak
        2 = nie
        """))
        if qq == 1:
            qqq = int(input("""
            1 = Ma kontakt z klientem
            2 = Nie ma kontaku z klientem
            """))
            if qqq == 1:
                self.kontaktk == "Ma kontakt z klientem"
            elif qqq == 2:
                self.kontaktk == "Nie ma kontaku z klientem"
        elif qq == 2:
            ("Nie wprowadzam zmian.")
        else:
            pass