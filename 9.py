# 1.Napisz “Timer” przyjmuje od użytkownika liczbę minut. Liczymy za ile skończy się czas. (program na rozgrzewkę)
# from time import sleep
# def qq():
#     q = float(input(":")) * 60
#     while q > 0:
#         print(f"zostało {q}s")
#         q -= 1
#         sleep(1)
#     print("END !!!")
# qq()
# 2.Stwórz krotkę/tuples zawierającą 6 elementów. Zmień ją na listę, usuń 2 ostatnie elementy i zmień z powrotem na krotkę.
# q = (1,2,3,4,5,6)
# w = list(q)
# w.pop()
# w.pop()
# q = tuple(w)
# print(w)
# 3.Napisz funkcję zwracającą krotki/tuples o losowych wartościach z przedziału 1,100.
# from random import randint
# print("-"*80)
# def q():
#     return tuple([randint(1,10) for i in range(randint(10,20))])
# print(q())
# print("-"*80)
# def w(data):
#     data = list(set(list(data)))
#     data.sort(reverse=True)
#     return tuple(data)
# print(w(q()))
# 4.Napisz funkcję która przepisze listę  moja lista na krotkę. 
# mylist = [1,2,3,4]
# print(mylist)
# k = tuple(mylist)
# print(k)
# # 5.Napisz funkcję która sprawdza czy zapytany element jest w set.
# q = {"kot","pies","krmuva"}
# def www(data):
#     qq = input()
#     odp = qq in data if "Tak" else "Nie"
#     print(odp)
# www(q)
# 6.Napisz funkcję która przyjmie nieskończenie wiele elementów i wyświetli które z nich występują w set klasa_1c . 
# klasa_1c = {"Ala","Maciek","Kasia", "olek", "Basia", "Wojtek"}
# def qq(inp_set, *data):
#     for i in data:
#         if i in inp_set:
#             print(f"{i} Jest")
#         else:
#             print(f"{i} Nie jest")
# qq(klasa_1c, "Ala" , "Maciek", "Bożydar")
# 7.Napisz program co przyjmuje symbol następnie
# go drukuje w podanej przez użytkownika liczbie kolumn i wierszy. 
# def qq():
#     znak = input("znak = ")
#     wier = int(input("wier = "))
#     kol = int(input("kol = "))
#     for i in range(kol):
#         print(f" {znak} "*wier)
# qq()
# 8.Napisz program co wyświetli tabliczkę mnożenia o n rozmiarze:
n = 9
q = [n+1 for n in range(n)]
w = q.copy()
for n in q:
    for m in q:
       print(f"{n*m}   ", end="\t")
    print("\n")