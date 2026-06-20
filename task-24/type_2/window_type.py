#задание 2416

# data = "AABECAEABECADA"
# chars = "AE"
# max_len = 0
# left = right = 0
# while right < len(data)- 1:
#     if data[right] in chars and data[right+1] not in chars:
#         right+=2
#         current_len= (right- left) // 2
#         max_len = max(max_len,current_len)
#     else:
#         right+=1
#         left = right
# print(max_len)
# #3

#задача 7272
# data = "CBAAAABABCBAAAB"
# pairs = ["AB","CB"]
# left = right = 0
# max_len = 0
# while right < len(data)-1:
#     pair = data[right] + data[right+1]
#     if pair in pairs:
#         lenght = (right - left)//2 +1 #!не забвать про +1!
#         max_len = max(max_len,lenght)
#         right +=2
#     else:
#         right +=1
#         left = right
# print(max_len)
#3 если своя data, 65 c файлом


