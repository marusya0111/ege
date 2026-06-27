# data = "abbacadbada"
#
# left =  0
# max_len = 0
# used = set()
# for right in range(len(data)):
#
#     while data[right] in used:
#         used.remove(data[left])
#         left+=1
#     used.add(data[right])
#
#     current_len = right - left +1
#
#     if current_len > max_len:
#         max_len = current_len
#         string = data[left:right+1]
# print(max_len,string)

data = "abbacadbada"

left = 0
last_pos = {}
string = ""
max_len = 0
for right in range(len(data)):
    ch = data[right]
    if ch in last_pos and last_pos[ch] >= left:
        left = last_pos[ch] + 1
    last_pos[ch] = right

    current_len = right - left + 1
    if current_len > max_len:
        max_len = current_len
        string = data[left:right + 1]
print(max_len, string)



