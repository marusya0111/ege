##задание 2416
# with open("../files/2416.txt") as f:
#     data = f.read()
# chars = "AE"
# breaks = []
# i = 0
# while i < len(data)- 1:
#     if data[i] in chars and data[i+1] not in chars:
#             i+=2
#     else:
#         i+=1
#         breaks.append(i)
#
# breaks.append(len(data) - 1)
#
# max_len = 0
# for i in range(1,len(breaks)):
#         distance =breaks[i]-breaks[i-1] -1 #обезопасить себя -> "-1"
#         max_len = max(max_len,distance)
# print(max_len//2)

#задание7272
data = "CBAAAABABCBAAAB"
pairs = ["AB","CB"]
breaks = []
i = 0
while i < len(data)-1:
    pair = data[i] + data[i+1]
    if pair in pairs:
        i+=2
    else:
        i+=1
        breaks.append(i)

breaks.append(len(data)-1)

max_len = 0
for i in range(1,len(breaks)):
    distance = breaks[i]-breaks[i-1] -1
    max_len = max(max_len,distance)
print(max_len//2)




