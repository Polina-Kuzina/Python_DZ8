def get_human():
    global human_list
    human_list = {'Фамилия' : input('Фамилия: '), 'Имя' : input('Имя: '), 'Должность' : input('Должность: '), 'Зарплата' : input('Зарплата: ')}
    return human_list

def get_number():
    return input('Введите номер телефона: ')

def search_human():
    return input('Введите фамилию сотрудника: ')

