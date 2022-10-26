def ar():
    x = []
    while True:
        a = input()
        if a == 'stop':
            break
        x.append(float(a))
    sum = 0
    licznik  = len(x) - 1
    while (licznik >= 0):
        sum = sum + x[licznik]
        licznik -= 1
    ar = sum/len(x)
    print(ar)

ar()

def har():
    x = []
    while True:
        a = input()
        if a == 'stop':
            break
        x.append(float(a))
    sum = 0
    licznik  = len(x) - 1
    while (licznik >= 0):
        sum = sum + 1/x[licznik]
        licznik -= 1
    ha = len(x)/sum
    print(ha)

har()