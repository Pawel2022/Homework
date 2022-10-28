# 5.Wygeneruj 3 listy korzystając z nowo poznanej metody. (sam wymyśl parametry).
from random import randint
qq = [randint(1,10000) for i in range(100)]
print(qq)
w = [i for i in range(100) if i % 5 == 0]
print(w)
r = [randint(1,100000) for i in range(100) if i % 100 == 0]
print(r)