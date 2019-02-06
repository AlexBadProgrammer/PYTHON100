#############################SLAYD 6 STROKI
####ZADANIE 1
# word = input('Введите фамилию:\n')
def list1(word):

    list_of_v = [i+3 for i in range(((len(word) % 5) + 2) * 2)]
    return list_of_v
# print(list1(word))

####ZADANIE 2

def list2(word):

    list_of_v = [i + 3 for i in range(((len(word) % 5) + 2) * 2)]
    list2 = list_of_v + [i+1 for i in list_of_v]
    return list2
# print(list2(word))

####ZADANIE3

def list3(word):
    list_of_v = [i + 3 for i in range(((len(word) % 5) + 2) * 2)]
    list2 = list_of_v + [i+1 for i in list_of_v]
    list3 = list2[1:-1]
    return list3
# print(list3(word))

####zadanie4
def list4(word):
    list = []
    list_of_v = [i + 3 for i in range(((len(word) % 5) + 2) * 2)]
    list2 = list_of_v + [i+1 for i in list_of_v]
    list = [list2[i] for i in range(1, len(list2), 3)]
    return list
# print(list4(word))

####ZADANIE5

def list5(word):
    n = int(input('Введите часть списка для отображения:\n'))
    list = []
    list_of_v = [i + 3 for i in range(((len(word) % 5) + 2) * 2)]
    list2 = list_of_v + [i+1 for i in list_of_v]
    list = [list2[i] for i in range((n - 1) * round(len(list2) / 3), round(n * len(list2) / 3))]
    return list
