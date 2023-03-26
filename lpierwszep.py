def rozloz(x):
    k = 2
    while x >= 2:
        while x % k == 0:
            print(str(x) + " ")
            x = int(x/k)
        k += 1
    print("1")
 
print("Podaj liczbę: ")
a = int(input())
rozloz(a)