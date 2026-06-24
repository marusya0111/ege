from string import digits, ascii_uppercase
#from string import printable

#ZADACHA1
# data = "XZ1234AZZ1234AAZZ"
# alph = digits + ascii_uppercase
# #0123456789ABCDEF
# bad = alph[16:]
# for i in bad:
#     data = data.replace(i," ")
# data = data.split()
# max_len = len(max(data, key=len))
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
# bad = alph[12:]
# cnt = max_len = 0
#
# with open("../files/2422.txt") as file:
#     data = file.readline()
#
# for sym in bad:
#     data = data.replace(sym," ")
#
# for element in data.split():
#     while element and element[0] == "0":
#         element = element[1:]
#     while element and element[-1] not in even:
#         element = element[:-1]
#     max_len = max(len(element),max_len)
#
# print(max_len)
#19

#-

