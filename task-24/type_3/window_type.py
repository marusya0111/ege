
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

# with open("../files/2422.txt") as file:
#     data = file.readline()

# right = left = 0
# for right in range(len(data)):
#     if data[right] in bad:
#         left = right +1
#         continue
#     while data[left] == "0":
#         left+=1
#     if data[right] in even:
#         max_len = max(max_len,right-left +1)
# print(max_len)
#5

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
# data = "LOCIZQT00795CCAELL"
#
# left = 0
# substring = 0
# for right in range(len(data)):
#     if data[right] in bad:
#         left = right+1
#     else:
#         continue
#     while data[left] == "0":
#         left+=1
#     if data[right] in even:
#         substring = data[left:right+1]
#         if substring:
#             substring.append((substring,right))
# ans = max(substring, key = lambda x : int(x[0],15))
# print(ans)



#22356 Текстовый файл состоит из десятичных цифр
# и заглавных букв латинского алфавита.
# Onределите в этом файле последовательность идущих подряд символов,
# представляющих собой запись максимального нечётного 12-ричного числа.
# В ответе запишите индекс (номер)
# первого символа (первой значащей цифры), с которого начинается запись
# этого числа в прилагаемом файле. Нумерация символов в текстовом файле начинается с нуля.

# from string import digits,ascii_uppercase
# alph = digits+ascii_uppercase
# good = alph[:12]#0123456789ABCDE
# bad = alph[12:]
# even = good[1::2]
# data = "LOCIZQT00795CCAELL"
# left = 0
# substring = 0
# substrings = []
# for right in range(len(data)):
#     if data[right] in bad:
#         left = right+1
#         continue
#     while left < right and data[left] == "0":
#         left+=1
#     if data[right] in even:
#         substring = data[left:right+1]
#         substrings.append((substring,left))
# ans = max(substrings, key = lambda x : int(x[0],12))
# print(ans)
#('795', 9)