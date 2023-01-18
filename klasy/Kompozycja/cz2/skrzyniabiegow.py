class Skrzyniabiegow():
    def __init__(self) -> None:
        self,__ilosc_biegow = None
        self,__jakaskrzynia = None

    def informacje(self):
        print("Informacje skrzyni biegu")
        print(self.__ilosc_biegow)
        print(self.__jakaskrzynia)

    def zmien_informacje_skrzyniabiegow(self):
        while True:
            print("="*40)
            print("2 - ilosc biegow 1 - jaka skrzynia 3 - exsit")
            inp = int(input())
            if inp == 1:
                print("1 - automat 2 - manual")
                iinp = int(input())
                self.__jakaskrzynia = iinp 
            elif inp == 2:
                inp = int(input())
                self.__iloscbiegow = inp 
            elif inp == "e":
                break  