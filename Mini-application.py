# Application show info, when you add data

Data = input('Введите значение("Да" или "Нет"):')

if Data == 'Да' or Data == 'да':
    FirstName = input('Укажите своё имя:')
    if not FirstName:
        print('Вы не ввели имя, введите повторно')
    while True:
        try:
            Age = int(input("Укажите свой возраст:"))
            break
        except ValueError:
            print('Вы не указали возраст, попробуйте ввести повторно')
    if Age < 0 or Age > 150:
        print("Вы указали неверное значение")
    elif Age > 0 or Age < 150:
        print('Привет,' + FirstName + '!', 'Тебе ' + str(Age), 'и это круто! :)')
elif Data == 'Нет' or Data == 'нет':
    Then = 'Оки, пока'
    print(Then)
else:
    print("Вы не выбрали \"Да\" или \"Нет\"")
