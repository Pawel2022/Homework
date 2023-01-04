from klasy import klas


print("""
Co chcesz zrobic?
1 = przeliczanie z km/h na m/s
2 = zamiana z t na g
3 = obliczanie predkosci (s,t)
4 = obliczanie czasu z prędkości
5 = obliczanie drogi z prędkości
6 = obliczanie prędkości średniej
7 = przyspieszenie
8 = obliczanie prędkości po przyspieszeniu
9 = odleglosc w ruchu jednostajnym prostoliniowym
10 = częstotliwość
11 = prędkośc kątowa
12 = chwilowa prędkość kątowa
13 = chwilowa prędkość kątowa
14 = prędkość liniowa
15 = prędkość liniowa z kątowej
16 = pszyspieszenie srednie
17 = siła wypadkowa
18 = przyspieszenie
""")
qpqp = int(input(""))
if qpqp == 1:
    klas.kilometrmetr()
elif qpqp ==2 :
    klas.tgg()
elif qpqp == 3:
    klas.vst()
elif qpqp == 4:
    klas.tvs()
elif qpqp == 5:
    klas.svt()
elif qpqp == 6:
    klas.vsr()
elif qpqp == 7:
    klas.a()
elif qpqp == 8:
    klas.va()
elif qpqp == 9:
    klas.odx()
elif qpqp == 10:
    klas.f()
elif qpqp == 11:
    klas.w()
elif qpqp == 12:
    klas.cpk()
elif qpqp == 13:
 klas.akat()
elif qpqp == 14:
    klas.plina()
elif qpqp == 15:
    klas.plzpk()
elif qpqp == 16:
    klas.ps()
elif qpqp == 17:
    klas.silw()
elif qpqp == 18:
    klas.ad()