from math import pi, pow, log
 
class Okrag():

    def __init__(self, promien) -> None:
        self.promien = promien
        self.pole_powieszchni = self.oblicz_pole_powierzchni(self.promien)
        self.informacje1()
       
    def oblicz_pole_powierzchni(self,promien):
        return pi*pow(promien,2)
 
    def zmien_promien(self,promien):
        self.promien = promien
        self.pole_powieszchni = self.oblicz_pole_powierzchni(self.promien)
 
    def informacje1(self):
        print("-"*40)
        print(f"Zadeklarowano Okrag")
        print(f"Dla pi = {pi}")
        print(f"Dla promienia = {self.promien}")
        print(self.pole_powieszchni)
        print("-"*40)

Okrag(100)

class szescian():

    def __init__(self, bok) -> None:
        self.bok = bok
        self.objetosc1 = self.oblicz_objetosc(self.bok)
        self.informacje2()

    def oblicz_objetosc1(self,bok):
        return bok**3

    def zmien_bok(self,bok):
        self.bok = bok
        self.objetosc1 = self.oblicz_objetosc1(self.bok)
    
    def informacje2(self):
        print("-"*40)
        print("Zadeklarowano sześcian")
        print(f"Dla boku = {self.bok}")
        print(self.objetosc1)
        print("-"*40)
        
szescian(2)

class vgraniastoslup:
    def __init__(self, bok1, bok2, bok3) -> None:
        self.bok1 = bok1
        self.bok2 = bok2
        self.bok3 = bok3
        self.objetosc2 = self.oblicz_objetosc2(self.bok1,bok2,bok3)
        self.informacje3()

    def oblicz_objetosc2(self,bok1,bok2,bok3):
        return bok1*bok2*bok3

    def zmien_boki1(self,bok1,bok2,bok3):
        self.bok1 = bok1
        self.bok2 = bok2
        self.bok3 = bok3
        self.objetosc2 = self.oblicz_objetosc2(self.bok1,bok2,bok3)

    def informacje3(self):
        print("-"*40)
        print("Zadeklarowane graniastoslup")
        print(f"""
        Dla bokow:
        1 = {self.bok1}
        2 = {self.bok2}
        3 = {self.bok3}
        {self.objetosc2}
        """)
        print("-"*40)

vgraniastoslup(1,2,3)

class prostopadloscian:
    def __init__(self,a,h,l) -> None:
        self.a = a
        self.h = h
        self.l = l
        self.obj = self.oblicz_obj(self.a,self.h,self.l)
        self.inf()

    def oblicz_obj(self,a,h,l):
        return a*h*l/2
        
    def zmien_boki(self,a,h,l):
        self.a = a
        self.h = h
        self.l = l
        self.obj = self.oblicz_obj(self.a,h,l)

    def inf(self):
        print("-"*40)
        print(f"""
        Zadeklarowano prostopadloscian
        dla a = {self.a}
        dla h = {self.h}
        dla l = {self.l}
        {self.obj}
        """)
        print("-"*40)

prostopadloscian(1,1,3)
class sinus:
    def __init__(self,a,c) -> None:
        self.a = a
        self.c = c
        self.ob = self.oblicz_ob(self,a,c)
        self.inf()

    def oblicz_ob(self,a,c):
        return a/c

    def zmien_boki(self,a,c):
        self.a = a
        self.c = c
        self.ob = self.oblicz_ob(self,a,c)

    def inf(self):
        print("-"*40)
        print(f"""
        Zadeklarowano sinus
        dla a = {self.a}
        c = {self.c}
        {self.ob}
        """)
        print("-"*40)

sinus(2,2)

class cos():
    def __init__(self,b,c) -> None:
        self.b = b
        self.c = c
        self.ob = self.oblicz_ob(self,b,c)
        self.inf()

    def oblicz_ob(self,b,c):
       return b/c

    def zmien_boki(self,b,c):
        self.b = b
        self.c = c
        self.ob = self.oblicz_ob(self,b,c)

    def inf(self):
        print("~"*40)
        print(f"""
        zadeklarowanoe cosinus
        dla b = {self.b}
        dla c = {self.c}
        {self.ob}
        """)
        print("~"*40)

cos(2,3)
class tg():

    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b
        self.ob = self.oblicz_ob(self,a,b)
        self.inf()

    def oblicz_ob(self,a,b):
        return a/b

    def zmien_boki(self,a,b):
        self.a = a
        self.b = b
        self.ob = self.oblicz_ob(self,a,b)

    def inf(self):
        print("-"*40)
        print(f"""
        Zadeklarowano tangens
        dla a = {self.a}
        b = {self.b}
        {self.ob}
        """)
        print("-"*40)

tg(2,2)

class pit():
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b
        self.ob = self.oblicz_ob(self,a,b)
        self.inf()

    def oblicz_ob(self,a,b):
        return a**2+b**2

    def zmien_boki(self,a,b):
        self.a = a
        self.b = b
        self.ob = self.oblicz_ob(self,a,b)

    def inf(self):
        print("-"*40)
        print(f"""
        Zadeklarowano pitagorasa
        dla a = {self.a}
        b = {self.b}
        {self.ob}
        """)
        print("-"*40)

pit(2,2)

class kolo():
    def __init__(self,r) -> None:
        self.r = r
        self.ob = self.oblicz_ob(self,r)
        self.inf()

    def oblicz_ob(self,a):
        return 2*pi*r

    def zmien_boki(self,r):
        self.r = r
        self.ob = self.oblicz_ob(self,r)

    def inf(self):
        print("-"*40)
        print(f"""
        Zadeklarowano obwod kola
        dla r = {self.r}
        pi = {pi}
        {self.ob}
        """)
        print("-"*40)

kolo(2)

class trapez():
    def __init__(self,a,b,h) -> None:
        self.a = a
        self.b = b
        self.h = h
        self.ob = self.oblicz_ob(self,a,b,h)
        self.inf()

    def oblicz_ob(self,a,b,h):
        return (a*b)/2*h

    def zmien_boki(self,a,b,h):
        self.a = a
        self.b = b
        self.h = h
        self.ob = self.oblicz_ob(self,a,b,h)

    def inf(self):
        print("-"*40)
        print(f"""
        Zadeklarowano pole trapezu
        dla a = {self.a}
        dla b = {self.b}
        dla c = {self.c}
        {self.ob}
        """)
        print("-"*40)

trapez(1,2,3)

class stozek():
    def __init__(self,r,h) -> None:
        self.r = r
        self.h = h
        self.ob = self.oblicz_ob(self,r,h)
        self.inf()

    def oblicz_ob(self,r,h):
        return 1/3*pi*r**2*h

    def zmien_boki(self,r,h):
        self.r = r
        self.h = h
        self.ob = self.oblicz_ob(self,r,h)

    def inf(self):
        print("-"*40)
        print(f"""
        Zadeklarowano objetosc stozka
        dla r = {self.r}
        dla h = {self.h}
        pi = {pi}
        {self.ob}
        """)
        print("-"*40)

stozek(1,2)
