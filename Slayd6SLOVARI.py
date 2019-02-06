#############################SLAYD 6 SLO
# print (u'\u044f \u0434\u043D\u043E \u043F\u0440\u043E\u0433\u0440\u0430\u043C\u043C\u0438\u0440\u043E\u0432\u0430\u043D\u0438\u044F')
####ZADANIE 1VARI
# word = input('Введите фамилию:\n')

def dict1(a):

    d = {i: i + 2 for i in range(((len(a) % 5) + 2) * 2)}
    return d
# print(dict1(a))

####ZADANIE 2
def dict2(word):

    d = {i: i + 2 for i in range(((len(word) % 5) + 2) * 2)}
    d.update({i + len(d): d[i]+1 for i in range(len(d))})
    return d
# print(dict2(word))

####ZADANIE 3
def dict3(word):

    d = {i: i + 2 for i in range(((len(word) % 5) + 2) * 2)}
    d.update({i+len(d): d[i]+1 for i in range(len(d))})
    d = {i: d[i] for i in range(1, len(d), 3)}
    return d
# print(dict4(word))

####ZADANIE 4

def dict4(word):

    d = {i: i + 2 for i in range(((len(word) % 5) + 2) * 2)}
    d.update({i+len(d): d[i]+1 for i in range(len(d))})
    d = {i: d[i] for i in range(1, len(d), 3)}
    return d
# print(dict4(word))

####ZADANIE 5

# n = int(input('Введите часть словаря для отображения:\n'))

def dict5(word):

    d = {i: i + 2 for i in range(((len(word) % 5) + 2) * 2)}
    d.update({i+len(d): d[i]+1 for i in range(len(d))})
    d = {i: d[i] for i in range((n - 1) * round(len(d) / 3), round(n * len(d) / 3))}
    return d
# print(dict5(word))