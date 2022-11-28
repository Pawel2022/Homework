math = []

users = [
    {
    "name":"Adam",
    "surname":"Kowalski",
    "age":15,
    },
    {
    "name":"Janusz",
    "surname":"Kowalski",
    "age":15,
    },
    {
    "name":"Piotr",
    "surname":"Nowak",
    "age":15,
    },
]
def print_users(data):
    for obj in data:
        for k, v in obj.items():
            print(f"{k}: {v}")
        print(f"""
        {"-"*10} \n
        """)
print_users(users)


def add_workers():
    new_dictionary = {}
    name = input("name:")
    new_dictionary["name:"] =name if name else " No Data"
    data = input("surname:")
    new_dictionary["surname:"] =data if data else " No Data"
    data = int(input("age:"))
    new_dictionary["age:"] =data if data else " No Data"
    users.append(new_dictionary)






def edit_users():
    for dic in users:
        inp = input("Podaj osobe")
        print("e - exit")
        if dic.get("name") == inp:  
            while True:
                print("""
                Co chcesz zmienic
                1 - name, 2 - surname
                3 - age , 4 - sto
                """)
                inp_num= int(input("Podaj liczbe"))
                if inp_num == 1:
                    inp = input("name ?")
                    dic["name"] = inp
                elif inp_num == 2:
                    inp = input("surname ?")
                    dic["surname"] = inp
                elif inp_num == 3:
                    inp = input("age ?")
                    dic["age"] = inp  
                elif inp_num == 4:
                    break
                else:
                    print("Nie ma takiej komendy")
                    continue
        elif inp == "e":
            break
        else:
            print("Nie ma takiej osoby")
print(users)
print("""1-add user
    2-control
""")
ch = int(input())


if ch == 1:
    add_workers()
    print(users)
elif ch == 2:
    edit_users()
    print(users)

