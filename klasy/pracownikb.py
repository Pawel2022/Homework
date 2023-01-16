from pracownikinny import pracownikinny
class pracownikb(pracownikinny):
    def __init__(self, oddzial, projekt, homeoffice, szef):
        self.oddzial = oddzial
        self.projekt = projekt
        self.homeoffice = homeoffice
        self.szef = szef

    def poddzial(self):
        print(self.oddzial)
        qq = int(input("""
        Czy chcesz zedytować
        1 = tak
        2 = nie
        """))
        if qq == 1:
            self.skarga = input("Nowy oddzial:")
        elif qq == 2:
            ("Nie wprowadzam zmian.")
        else:
            pass

    def pprojekt(self):
        print(self.projekt)
        qq = int(input("""
        Czy chcesz zedytować
        1 = tak
        2 = nie
        """))
        if qq == 1:
            self.skarga = input("Nowy projekt:")
        elif qq == 2:
            ("Nie wprowadzam zmian.")
        else:
            pass

    def phomeoffice(self):
        print(self.homeoffice)
        qq = int(input("""
        Czy chcesz zedytować
        1 = tak
        2 = nie
        """))
        if qq == 1:
            qqq = input(input("""
            1 = homeoffice
            2 = w biurze
            """))
            if qqq == 1:
                self.hoemoffice = "homeoffice"
            elif qqq == 2:
                self.homeoffice = "biuro"
        elif qq == 2:
            ("Nie wprowadzam zmian.")
        else:
            pass

    def pszef(self):
        print(self.szef)
        qq = int(input("""
        Czy chcesz zedytować
        1 = tak
        2 = nie
        """))
        if qq == 1:
            self.szef = input("Nowy szew:")
        elif qq == 2:
            ("Nie wprowadzam zmian.")
        else:
            pass