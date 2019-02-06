# ############SLAYD 7 GOTOV
#
# ###ZADANIE 1
#
def stroka(n):
    s = 'bla-'
    return n*s
# print(str(5))
# print(u'\u2603 \u26C7 ')
###ZADANIE 2

# a = int(input('сколько раз \n'))
# x = (input('а здесь строку \n'))


def lesenka(n):
    pr = '='
    for i in range(0, n + 1):
        print(pr * i * 3)

###ZADANIE 3 ПОЧЕМУ-ТО ДУБЛИРУЕТСЯ ОТВЕТ

#### chars = "abcdefghijklmnopqrstuvwxyz"
'''s = input(str("VVEDITE SLOVO \n"))'''
def skolko(s):
    for char in s:
        count = s.count(char)
        # if count > 1:
        print(count, char)
''' print(skolko(s))'''
# print(u'\u2603 \u26C7 ')

###zadanie 4

# a = input('Введите предложение:\n')
def dlinna(a):
    dlina = {}
    for word in a.split():
        key = 'слов длинной ' + str(len(word))
        if key in dlina:
            dlina[key] += 1
        else:
            dlina[key] = 1
    return dlina
# print(dlina(a))
# print(u'\u2603 \u26C7 ')

