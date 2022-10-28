# 6.Funkcję która generuje listę 10 liczb która nie jest podzielna 2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88.
from random import randint
q = [randint(0,100**2) for i in range(0,10) if i % 2 != 0 and i % 3 != 0 and i % 4 != 0 and i % 4 != 0 and i % 5 != 0 and i % 6 != 0 and i % 7 != 0 and i % 8 != 0 and i % 9 != 0 and i % 11 != 0 for i in range(0,10) ] 
print(q)