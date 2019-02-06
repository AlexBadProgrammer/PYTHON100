####SLAYD9

###ZADANIE 1-2
# # первый и второй члены последовательности равны 1, каждый следующий
# # равен сумме двух предыдущих (1, 1, 2, 3, 5, 8, 13, ...)
def fibon():
    N = int(input('Сколько членов последоательности вывести\nчисло\n '))
    M = int(input('Здесь скажи сколько будет первых единиц\nчисло(на 1 ловит баг)\n '))
    fib = [1 for _ in range(M)]
    while len(fib) <= N:
        f = 0
        for i in range(1, M + 1):
            f += fib[-i]
        fib.append(f)
    return fib
# print(fibon(N,M))

###ZADANIE 3

def kvadrat():
    n = int(input('введите число\n'))
    return [n**2 for n in range(1, n+1, 2)]
# print(kvadrat(n))

###ZADANIE 4

def ramka():
    x = int(input('Введите ширину:\n'))
    y = int(input('Введите высоту:\n'))
    s = '*'
    for i in range(y+1):
        if i == 0 or i == y:
            print(s*x)
        else:
            print(s + ' '*(x-2) + s)
# print(ramka(x,y))

###ZADANIE 5
##а что бы вывести один ответ под другим нужно функцию для каждого аргумента отдельно вызывать?

def natur():
    a = int(input('Введите 1-ое число\n'))
    b = int(input('Введите 2-ое число\n'))
    summa = 0
    proizv = 1
    for i in range(a,b + 1):
        summa += i
        proizv *= i
    return summa, proizv
# print('Сумма и произведение \nнатуральных чисел включительно\n', natur(a,b))


###ZADANIE 6
#Даны натуральные числа А и В. Вывести сначала все чётные числа, заключённые между ними, потом все нечётные
def chisla():
    a = int(input('Введите 1-ое число\n'))
    b = int(input('Введите 1-ое число\n'))
    chet = []
    nechet = []
    for i in range(a,b+1):
        if i % 2 == 0:
            chet.append(i)
        else:
            nechet.append(i)
    return chet, nechet
# print('Четные и нечетные\nмежду ними\n',chisla(a,b))

###ZADANIE 7
#Исходный список содержит положительные и отрицательные числа. Требуется положительные поместить в один список, а отрицательные - в другой
def znak():
    a = [20, -8, -10, 84, -45, 80, -6, 7, 9, -1, 22, -59]
    pol = [i for i in a if i >= 0]
    otr = [i for i in a if i < 0]
    return pol, otr
# print('     Слева положительные, справа отрицательные\n',znak(a))