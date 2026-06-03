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
with open ("../files/2401.txt") as f:
    data = f.readline()

cur = 1
max_len = 0
#abcdadida
for i in range(len(data)-1):
    if data[i] + data[i+1] in ("ad","da"):
        cur=1
    else:
        cur+=1
    max_len = max(cur, max_len)
print(max_len)

