# 8.Funkcja która skopiuje i zwrócił listę w której występuje największy element.
import copy
def gg():
    a=[1,2,333,4,1,2,3,4,]
    b=[11,2,3,4,31]
    c=[5,9,2344,0]
    e = (a,c)
    d = copy.copy(e)
    x = None
    for i in d:
        
        if x == None or x < i:
            x = i
    print(x)
gg()