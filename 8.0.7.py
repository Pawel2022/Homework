# 7.Funkcję która generuje listę 10 liczb która nie jest podzielna przynajmniej przez jedną z liczb
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41.
from random import randint
def qq():
    q = [randint(0,100**2) for i in range(0,10) if i % 2 != 0 or i % 3 != 0 or i % 5 != 0 or i % 7 != 0 or i % 11 != 0 or i % 13 != 0 or i % 17 != 0 or i % 19 != 0 or i % 23 != 0 or i % 29 != 0 or i % 31 != 0 or i % 37 != 0 or i % 41 != 0]
    print(q)
qq()