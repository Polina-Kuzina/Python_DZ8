def look_personal_base():
    data = open(r'Personal_base\Prog\persons.txt', 'r')
    for line in data:
        print(line)
    data.close()
