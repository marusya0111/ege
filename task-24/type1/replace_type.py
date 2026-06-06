                    #TYPE1
#1задача
# data = "ABCAABACACAB"
# #A BCAA BACACA B
# data = data.replace("AB","A B")
# data = data.split()
# answer = max(data, key = len)
# an =max( map(len,data))
# print(data,len(answer),an)

#2задача
#    1 способ
#adacacadacadiidardtad
# with open ("../files/2401.txt") as f:
#     data = f.readline()
#     #делим по сегментам
#     data = data.replace("ad","a d").replace("da", "d a")
#     answer = len(max(data.split(), key=len))
#     print(answer)
#2252


#    2 способ
# with open ("../files/2401.txt") as f:
#     data = f.readline()
#
# cur = 1
# max_len = 0
# #abcdadida
# for i in range(len(data)-1):
#     if data[i] + data[i+1] in ("ad","da"):
#         cur=1
#     else:
#         cur+=1
#     max_len = max(cur, max_len)
# print(max_len)


#Текстовый файл состоит из арабских цифр (0, 1, …, 9).
# Определите максимальное количество идущих подряд символов
# в прилагаемом файле, среди которых нет символов 0, стоящих рядом.

# with open("files/2410.txt") as file:
#     data = file.read()
#     while "00" in data:
#         data = data.replace("00","0 0")
#         answer = len(max(data.split(), key=len))
#     print(answer)




                    #TYPE2
#1zadacha
# with open("files/2417.txt") as file:
#     data = file.read()
#     data = data.replace("Q", "*").replace("R", "*").replace("S", "*")
#
#     while "**" in data:
#         data = data.replace("**","* *")
#     data = data.split()
#     answ = max(data,key = len)
#     print(len(answ))


#2zadacha
# 1 sposob
#with open("../files/16333.txt") as file :
#     data = file.read()
#     for i in "QRW":
#         data = data.replace(i, "@")
#
#     for p in "124":
#         data = data.replace(p, "*")
#
#     while "@@" in data or "@@" in data:
#         data = data.replace("@@","@ @")
#         data = data.replace("**","* *")
#
#     data = data.split()
#     answ = max(data,key = len)
#     print(len(answ))
#ответ 17

#2sposob
#data = data.translate(str.maketrans("QRW124","@@@***"))


#ЖАДНЫЙ ЛИНЕЙНЫЙ СПОСОБ
# data = "QRW1Q111111242QQQQ1"
# data = data.translate(str.maketrans("QRW124","@@@***"))
#
# max_len = 1
# current_len = 1
# for i in range(1,len(data)):
#     if data[i] != data[i-1]:
#         current_len += 1
#         max_len = max(max_len,current_len)
#     else:
#         current_len = 1
# print(max_len)

#3sposob плавующее окно, перескакиваем из left в right
# data = "QRW1Q111111242QQQQ1"
# data = data.translate(str.maketrans("QRW124","@@@***"))
#
# left = 0
# max_len = 0
# for right in range(1,len(data)):
#     if data[right] == data[right-1]:
#         left = right
#
#     current_len = right - left + 1
#
#     max_len = max(max_len, current_len)
# print(max_len)


#3zadacha
# with open("../files/13866.txt") as file :
#         data = file.read()

#         for i in "13579":
#             data = data.replace(i, "@")
#
#         while "@@@" in data:
#             data = data.replace("@@@", "@ @ @")
#
#         data = data.split()
#         answ = max(data,key = len)
# print(len(answ))
#2580

data = "111AAAA333"
data = data.translate(str.maketrans("13579", "*****"))
current_len = 2
max_len=  0
for i in range(2,len(data)):
    current_len +=1
    if data[i] == data[i - 1] == data[i-2] == "*":
            current_len= 2

    max_len = max( max_len,current_len)
    print(max_len)