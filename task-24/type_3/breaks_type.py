#2422 Текстовый файл состоит из символов, обозначающих десятичные цифры
# и заглавные буквы латинского алфавита. Определите в прилагаемом
# файле максимальное количество идущих подряд символов,
# которые могут представлять запись чётного числа в двенадцатеричной
# системе счисления. В этой записи отсутствуют незначащие (ведущие) нули.

from string import digits,ascii_uppercase
alph = digits + ascii_uppercase
data = "XX02345A1XX"
even = alph[:12:2]
good= alph[:12]
bad = alph[12:]
cnt = max_len = 0

i = 0
breaks = []
while i in range (len(data)):
    if data[i] in bad:
        breaks.append(i)

breaks.append(len(data))
distance = 0
max_len = 0
for i in range(1,len(breaks)):
    part = data[breaks[i-1]+1 : breaks[i]]
    while part and part[0] =="0":
        part= part[1:]
        while part and part[-1] not in even:
            part = part[:-1]
        distance = max(distance,len(part))
print(distance)

