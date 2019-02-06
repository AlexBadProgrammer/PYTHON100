###########SLAYD 11

###Zadanie2
def razr(vvod):
    vvod = int(input('Введите число\n'))
    vvod = abs(vvod)
    count = 1
    vvod //= 10
    while vvod > 0:
        vvod //= 10
        count += 1
    return count
# print('Количество разрядов в этом числе\n',razr(vvod))

####ZADANIE 3
def palindrom():
    slovo = str(input('Игра "Палиндром"\n Введите слово \n'))
    l = len(slovo)
    for i in range(l//2):
        if slovo[i] != slovo[-1-i]:
            res = 'Не палиндром!'
            break
        else:
            res = 'Палиндром!'
    return res
# print(palindrom(slovo))

###ZADANIE 4


def rep():
    stroka = input('введите строку\n')
    old = input('какиое слово заменить?\n')
    new = input('на какое\n')
    print(stroka.replace(old, new, ))


#TUT ZHEST', 4ERT NOGU SLOMET, V INETE NASHEL, SAM NE OCHEN' PONIMAU KAK RABOTAET. NO ONO PASHET
# def mass_replace():
#     text = {'The dog hunts the cat'}
#     dct = {}
#     new_string = {"dog":"cat", "cat":"dog"}
#     old_string = text
#     while len(old_string) > 0:
#         s = ""
#         sk = ""
#         for k in dct.keys():
#             if old_string.startswith(k):
#                 s = dct[k]
#                 sk = k
#         if s:
#             new_string += s
#             old_string = old_string[len(sk):]
#         else:
#             new_string += old_string[0]
#             old_string = old_string[1:]
#     return new_string

# print(mass_replace("The dog hunts the cat", {"dog":"cat", "cat":"dog"}))
# print('изначальная строка \nThe dog hunts the cat"')


