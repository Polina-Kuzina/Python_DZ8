import In
import Prog
import Out



def personal_base():
    while True:
        print('Список комманд:\n 1 - Добавить сотрудника\n 2 - Посмотреть список сотрудников\n 3 - Завершить работу \n')
        command = int(input('Введите номер команды: '))
        if command == 1:
            f = 1
            while f:
                fio_new = In.get_human()
                Prog.add_person(fio_new)
                print(f'Данные успешно сохранены')
                f = int(input('Хотите записать еще сотрудника? (1 - да, 0 - нет) '))               
        elif command == 2:
            print('Список сотрудников: \n')
            Out.look_personal_base()              
        elif command == 3:
            print('До новых встреч!')
            break
        else:
            print('Введите корректную команду')

        
