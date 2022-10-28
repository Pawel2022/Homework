# 4.Funkcję która zamieni 2 wartości x i y. Zakładając że  x i y występują poza funkcją (Global).
x = 21
y = 37
def qq():
    global x,y
    x,y = y,x
    print(x,y)

qq()
