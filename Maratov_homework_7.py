while 1:
    number = num = int(input('Введите число: '))
    mun = 0
    if 99 < num < 1000:
        while num > 0:
            x = num % 10
            num = num // 10
            mun = mun * 10
            mun = mun + x
            if mun > 99:
                if mun == number:
                    print(True,'\n')
                else:
                    print(False,'\n')

    elif 0 <= num <= 99 or 999 < num < 1000000:
        print('Вы ввели не трехзначное число!\n')
    elif num < 0:
        print('Отрицательное число считается не универсальным!\n')
    else:
        print('Вы ввели неверное число!\n')
