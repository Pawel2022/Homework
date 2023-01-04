from math import pi
class klas:
    @staticmethod
    def kilometrmetr():
        qqq = float(input(":"))
        
        print(f"Wynik wynosi {qqq*1000/3600} m/s.")
    
    def tgg():
        qqq = float(input(":"))
        print(f"Wynik wynosi {qqq*1000000}")
    
    def vst():
        s = float(input("(m)"))
        t = float(input("(s)"))
        print(f"Wynik wynosi {s/t}m/s")
    
    def tvs():
        v = float(input("(m/s)"))
        s = float(input("(m)"))
        print(f"Czas wynosi {s/v}")
    
    def svt():
        v = float(input("(m/s)"))
        t = float(input("(s)"))
        print(f"Droga wynosi {t*v} s.")
    
    def vsr():
        s = float(input("(m)"))
        t = float(input("(s)"))
        print(f"Prędkość średnia {s/t} m/s")
    
    def a():
        v = float(input("(m/s)"))
        t = float(input("(s)"))
        print(f"Wynik wynosi {v/t}")
    
    def va():
        vo = float(input("vo = "))
        a = float(input("a = "))
        t = float(input("t = "))
        print(f"Wynik wynosi {vo+a*t}")
    
    def odx():
        xo = float(input("xo = "))
        vo = float(input("vo = "))
        t = float(input("t = "))
        a = float(input("a = "))
        print(f"Wynik wynosi {xo+vo*t+0,5*a*t*t}")
    
    def f():
        n = float(input("n="))
        t = float(input("t="))
        print(f"Wynik wynosi {n/t} Hz.")

    def w():
        kat = float(input("kat="))
        t = float(input("t="))
        print(f"Wynik wynosi {kat/t}")

    def cpk():
        kat = float(input("kat="))
        t = float(input("t="))
        print(f"Wynik wynosi {kat/t} Hz.")

    def akat():
        pkat = float(input("zmiana prędkości kątowej = "))
        t = float(input("t="))
        print(f"Wynik wynosi {pkat/t}")

    def plina():
        r= float(input("r = "))
        tt = float(input("T = "))
        print(f"Wynik wynosi {2*pi*r/tt}")

    def plzpk():
        w = float(input("w = "))
        r = float(input("r = "))
        print(f"Wynik wynosi {w*r}")

    def ps():
        v = float(input("roznica v"))
        t = float(input("roznica t = "))
        print(f"Wynik wynosi {v/t}")

    def silw():
        m = float(input("masa = "))
        a = float (input("przyspieszenie = "))
        print(f"Wynik wynosi {m*a}")

    def ad():
        ff = float(input("f = "))
        m = float(input("m = "))
        print(f"Wynik wynosi {ff/m}")