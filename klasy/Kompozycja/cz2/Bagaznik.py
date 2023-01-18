class Bagaznik:
    def __init__(self) -> None:
        self,__wielkosc = None
        self,__swiatelko = None

    def informacje(self):
        print("Dane silnika")
        print(self.__wielkosc)
        print(self.__swiatelko)

    def zmien_informacje_bagaznika(self):
        while True:
            print("="*40)
            print("1 - wielkosc 2 - swiatelko 3 - exit")
            inp = int(input())
            if inp == 1:
                inp = int(input())
                self.__wielkosc = inp 
            elif inp == 2:
                inp = int(input())
                self.__swiatelko = inp 
            elif inp == 3:
                break  