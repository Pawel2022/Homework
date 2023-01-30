# 1. Wyświetl (kocham_inf ):
# -Całą zawartość pliku.
# -każdą linjkę pokoleii
# -Pokolei każdy znak w nowej linijce.
# -Co 2 znak.
# -Jeśli znak równa się znakowi wprowadzonemu przez użytkownika wyświetl te znaki.
# -Jeśli znak równa się znakowi wprowadzonemu przez użytkownika wyświetl tą linijkę.
# -Wyświetl pierwsze 10 znaków.
# -Wyświetl ostanie 10 znaków.
# -Policz ile występuje znaków a, b i c.
class wyswietlzawartoscpliku:
    with open('kocham_inf.txt','r') as myfile:
        obj = myfile.read()
        ('-'*70)
        print(myfile)
        print('-'*70)
        print(obj)
        print('-'*70)
class wyswietllinijkipokoleji:
    with open('kocham_inf.txt', 'r') as my_file:
        for i in my_file:
            print('-'*70)
            print(i)
class wyswietlpokolejiznaki:
    with open('kocham_inf.txt','r') as my_file:
        obj = my_file.read()
        for i in obj:
            print(i)
class wyswietlco2znak:
    with open('kocham_inf.txt','r') as my_file:
        for line in my_file:
            print(line[::2])
class wyswietlznakwprowadzony:
    inp = input().lower()
    print('-'*70)
    with open('kocham_inf.txt', 'r') as my_file:
        all_txt = my_file.read()
        for letter in all_txt:
            if inp == letter.lower():
                print(f'{inp} \t {letter}')
class wyswietlznkailinijke:
    inp = input().lower()
    with open('kocham_inf.txt', 'r') as my_file:
        for line in my_file:
            if inp in line:
                print(line)
class wyswietlpierwsze10znakow:
    with open('kocham_inf.txt', 'r') as my_file:
        text = my_file.read()
        print(text[0:10:])
        print(len(text[0:10:]))
class wyswietlostatnie10znakow:
    with open('kocham_inf.txt','r') as my_file:
        text = my_file.read()
        print(text[-1:-12:-1])
        print(len(text[-1:-12:-1]))
class policznznaki:
    with open('kocham_inf.txt','r') as my_file:
        a_sum = 0
        b_sum = 0
        c_sum = 0
        for line in my_file:
            for let in line:
                a_sum = a_sum + 1 if let == 'a' else a_sum
                b_sum = b_sum + 1 if let == 'b' else b_sum
                c_sum = c_sum + 1 if let == 'c' else c_sum
    print(f'a_sum = {a_sum}')
    print(f'b_sum = {b_sum}')
    print(f'c_sum = {c_sum}')

# 2.Przepisz (kocham_inf) co do pliku tekstowego kocham_inf_2.
# -przepisz co 2 literę z  kocham_inf_2 do kocham_inf_3
# -przepisz n krotnie zawartość kocham_inf_2  do kocham_inf_4
class przepisanie:
    with open('kocham_inf.txt', 'r') as my_tet_file:
        text = my_tet_file.read()
    with open('kocham_inf_2.txt','a') as my_tet_file:
        my_tet_file.write(text)
class przepisco2litetr:
    def kocham_inf_3 (text):
        with open ('kocham_inf_3.txt', 'a') as my_txt_file:
            my_txt_file.write(text)
    with open('kocham_inf_2.txt', 'r') as my_txt_file:
        final_text = ''
        for line in my_txt_file:
            new_line = ''
            for i in range(len(line)-1):
                letter = line[i] if i%2==0 else ''
                new_line += f'{letter}'
            final_text += f'{new_line} \n'
        kocham_inf_3(final_text)
class przepisanienkrotniezinf3doinf4:
    def kocham_inf_4(n):
        with open('kocham_inf_2.txt', 'r') as my_txt_file_1:
            txt = my_txt_file_1.read()
            for i in range(n):
                with open ('kocham_inf_4.txt', 'a') as my_txt_file_2:
                    my_txt_file_2.write(txt)
# 3.Stóż n plików texstowych. Niech każdy z nich zawiera (kocham_inf + nr )
class zadanie3:
    n = int(input())
    for n in range(n):
        with open(f'filne{n}','w') as my_file:
            my_file.write(f'kocham_inf {n}')
# 4.Zwóż plik texstowy kocham_inf_22 zapisz w nim zawtość pliku kocham_inf w odwróconej kolejności.
class zadanie4:
    with open('kocham_inf', 'r') as myfile:
        inf = myfile.read()
    inf = inf[::-1]
    with open('kocham_inf_22', 'w') as myfile:
        myfile.write(inf)
# 5.Napisz program który:
# -stworzy n pików
# -o k nazwie + numer
# -Każdy zawierający m linijek
# -Stingu podanego przez użytkownika
class zadanie5:
    def czesc1():
        n = int(input('n_pikow = ? '))
        k = input('k_nazwie = ? ')
        m = int(input('m_linijek = ? '))
        co = input('co = ? ')
        for n in range(n):
            with open(f'{k}{n}.txt', 'a') as myfile:
                m_inp = m
                for m_inp in range(m):
                    myfile.write(f'{co} \n')
                myfile.write(f'\n')
# 6. Napisz funkcję generującą listę [1,2,3,4,5,6,7,8,9,10]. Następnie umieść te elementy w n linijkach w pliku tekstowym 
class zadanie6:
    def generator():
        lista = [i for i in range(1,10+1)]
        n = int(input(' n = '))
        with open ('xxx.txt', 'w') as myfile_2:
            for i in range(n):
                for i in lista:
                    myfile_2.write(f"{i} ")
                myfile_2.write(f"\n")
            print('*'*100)
    generator()
# 7. Napisz funkcję generująca tablę z tabliczką mnożenia o n wielkości. Następnie zapisz ją z pliku tekstowym.
class zadanie7():
    def generator2():
        inp = int(input('inp = '))
        with open('xxx_2.txt','w') as myfile:
            for i in range(1,inp+1):
                for n in range (1,inp+1):
                    myfile.write(f'{i*n}\t')
                myfile.write(f'\n')
    generator2()
# 8. Napisz funkcję która będzie dodawała do pliku textowego nowe inf (imię, nazwisko, miasto, telefon).
class adduser():
    def dodawanie():
        with open ('inf.txt','a')  as myfile:
            while True:
                print('E - exit the program')
                print('A - add a new user')
                inp = input()
                if inp.upper() == 'A':
                    imie = input('imię \t')
                    imie = imie.strip() if imie else None
                    nazwisko = input('nazwisko \t')
                    nazwisko = nazwisko.strip() if nazwisko else None
                    miasto = input('miasto \t')
                    miasto = miasto.strip() if miasto else None
                    telefon = input('telefon \t')
                    telefon = telefon.strip() if telefon else None
                    string_imp = f'{imie} {nazwisko} {miasto} {telefon} \n'.strip()
                    myfile.write('\n')
                    print('user added')
                    myfile.write(string_imp)
                elif inp.upper() == 'E':
                    print('Task End')
                    break
                else:
                    print('There is no such command')
    dodawanie()
