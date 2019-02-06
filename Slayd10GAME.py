import random

zanovo = 'да'
z = 0
while zanovo == 'да':

    zagadannoe = random.randint(1, 100)
    user_input = int(input('Игра " быдло-угадайка"\nЧИСЛО ДАВАЙ\n '))
    z += 1

    while user_input != zagadannoe and z != 5:
        if user_input < zagadannoe:
            user_input = int(input('ЧЕ ТАК мало\n'))
            z += 1
        elif user_input > zagadannoe:
            user_input = int(input('ВОУ-ВОУ, много\n'))
            z += 1
        else:
            print('угадал за\n', z)

    if z >= 5:
        print('чет дохера попыток')
        zanovo = input('Заново(да,нет)\n')