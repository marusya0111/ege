#ZADACHA1
# from string import digits, ascii_uppercase
# data = "XZ1234AZZ1234AAZZ"
# alph = digits + ascii_uppercase
# #0123456789ABCDEF
# bad = alph[16:]
# good = alph[:16]
# max_len = 0
# cnt = 0
# for i in range(len(data)):
#     if data[i] in good:
#         cnt+=1
#     else:
#         cnt = 0
#     max_len = max(max_len,cnt)
# print(max_len)

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
# cnt = max_len = 0
#
# with open("../files/2422.txt") as file:
#     data = file.readline()
#     for i in range(len(data)):
#         if cnt == 0 and data[i] == "0":
#             continue
#         if data[i] in good:
#             cnt+=1
#             if data[i] in even:
#                 max_len = max(max_len, cnt)
#         else:
#             cnt = 0
#     print(max_len)

# Текстовый файл состоит из десятичных цифр и
# заглавных букв латинского алфавита.
# Onределите в этом файле последовательность
# идущих подряд символов, представляющих собой
# запись максимального кратного пяти 15-ричного числа.
# В ответе запишите индекс (номер) последнего символа
# (последней значащей цифры), которой заканчивается
# запись этого числа в прилагаемом файле.
# Нумерация символов в текстовом файле начинается с нуля.

# from string import digits,ascii_uppercase
# alph = digits+ascii_uppercase
# good = alph[:15]#0123456789ABCDE
# bad = alph[15:]
# even = good[::5]
#
# data = "LOCIZQT00795CCAELL"
# cnt = 0
# max_len = 0
# index = 0
# string = ""
#
# for i in range(len(data)):
#     if string == "" and data[i] == "0":
#         continue
#     if data[i] in good:
#         string+= data[i]
#     else:
#         string = ""
#     if data[i] in even and max_len < int(string,15):
#         max_len = int(string,15)
#         index = i
# print(good)
# print(data[index - max_len +1 : index])
# #14
# 1