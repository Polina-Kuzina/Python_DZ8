def add_person(fio):
    with open(r'Personal_base\Prog\persons.txt', 'a') as data:
        data.write(f"{fio} \n")

