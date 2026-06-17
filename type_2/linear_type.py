#задание 2416
# data = "AABECAEABECADA"
# chars = "AE"
# i = 0
# cnt = 0
# max_len = 0
# while i < len(data)- 1:
#     if data[i] in chars and data[i+1] not in chars:
#         i+=2
#         cnt+= 1
#         max_len = max(cnt, max_len)
#     else:
#         i+=1
#         cnt= 0
# print(max_len)
#3

#задание 7272
# data = "CBAAAABABCBAAAB"
# pairs = ["AB","CB"]
# i = 0
# max_len = 0
# current_len = 0
# while i < len(data)-1:
#     pair = data[i] + data[i+1]
#     if pair in pairs:
#         i+=2
#         current_len += 1
#         max_len = max(max_len, current_len)
#     else:
#         i+=1
#         current_len = 0
# print(max_len)







