##########SLAYD 8

###Zadanie 1
#нужно вводить (сколько дней пройдет когда я пробегу ???км)
def beg1(km):

    i = 0
    x = 0
    while i < km:
        x += 1
        i += 2**x
    return x
# print(beg1(1000))

###Zadanie 2
##Каждый день я пробегаю «следующее простое число» км. Сколько дней пройдет, пока я в сумме пробегу 1000 км? 1000?

def begotnya2(km):
    lst = []
    days = 0
    n = 100
    itog = 0
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    while itog < km:
        itog += lst[days]
        days += 1
    return days, itog
# print(begotnya2(1000))

###ZADANIE 3
#Спортсмен трени­руется каждый день. Какой суммарный путь он пробежит за 30 дней
def begotnya3(d):
    itog = 0
    n = 1
    s = 10
    while n <= d:
        if n % 2 == 0:
            s *= 1.15
        itog += s
        n += 1
    return round(itog,3)
# print(begotnya3(10))

###ZADANIE 4
#Через сколько дней:
#а) спортсмен будет пробегать в день больше 20 км
def begotnya41(km):
    s = 10
    d = 1
    while s <= km:
        s *= 1.1
        d += 1
    return d
# print(begotnya41(15))
#b) пробежит суммарный путь 100 км
def begotnya42(km):
    res = 0
    s = 10
    d = 1
    while res <= km:
        res += s
        s *= 1.1
        d += 1
    return d
# print(begotnya42(100))

####почему-то возвращает только первый день в задаче ниже
# def begotnya4(km):
#     km = 10
#     summ = 10
#     i = 1
#     procent = 0.1
#     while summ < 100 and km < 20:
#         km = km + km * procent
#         summ = summ + km
#         i += 1
#         return i,km,summ
# print(begotnya4(0))