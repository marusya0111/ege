#2422 Текстовый файл состоит из символов, обозначающих десятичные цифры
# и заглавные буквы латинского алфавита. Определите в прилагаемом
# файле максимальное количество идущих подряд символов,
# которые могут представлять запись чётного числа в двенадцатеричной
# системе счисления. В этой записи отсутствуют незначащие (ведущие) нули.

# from string import digits,ascii_uppercase
# alph = digits + ascii_uppercase
# data = "XX02345A1XX"
# even = alph[:12:2]
# good= alph[:12]
# bad = alph[12:]
# cnt = max_len = 0
#
# i = 0
# breaks = []
# while i in range (len(data)):
#     if data[i] in bad:
#         breaks.append(i)
#
# breaks.append(len(data))
# distance = 0
# max_len = 0
# for i in range(1,len(breaks)):
#     part = data[breaks[i-1]+1 : breaks[i]]
#     while part and part[0] =="0":
#         part= part[1:]
#         while part and part[-1] not in even:
#             part = part[:-1]
#         distance = max(distance,len(part))
# print(distance)

# Текстовый файл состоит из десятичных цифр и
# заглавных букв латинского алфавита.
# Onределите в этом файле последовательность
# идущих подряд символов, представляющих собой
# запись максимального кратного пяти 15-ричного числа.
# В ответе запишите индекс (номер) последнего символа
# (последней значащей цифры), которой заканчивается
# запись этого числа в прилагаемом файле.
# Нумерация символов в текстовом файле начинается с нуля.

from string import digits,ascii_uppercase
alph = digits+ascii_uppercase
good = alph[:15]#0123456789ABCDE
bad = alph[15:]
even = good[::5]

substring = 0
cnt = max_len = 0
i = 0
breaks = [0]
part = 0
data = "LOCIZQT00795CCAELL"
for i in range(len(data)):
    if data[i] in bad:
        breaks.append(i)
candidats = []
breaks.append(len(data))
max_len = 0
for i in range(1,len(breaks)):
    left = breaks[i-1] + 1
    right = breaks[i]
    substring = data[left:right]
    if substring:
            substring.append((substring,right))

    while part and part[0] == "0":
        part = part[1:]

    for j in range(len(part)-1,-1,-1):
        if part[j] in even:
            number = part[:j+1]
            end_index = right - (len(part) -j )
            candidats.append((number,end_index))
ans = max(candidats, key = lambda x : int(x[0],15))

1






