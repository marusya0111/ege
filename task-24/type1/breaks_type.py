data = "QRW1Q112424QQQ1"
#       01    6789   12 13
with open("../files/16333.txt") as file:
    data = file.read()
    data = data.translate(str.maketrans("QRW124","aaa000"))
    #список ошибок
    breaks = []
    for mistake in range(1,len(data)):
        if data[mistake] == data[mistake - 1]:
            breaks.append(mistake)

    breaks.append(len(data)-1)

    max_len = 0
    for i in range(1,len(breaks)):
        distance =breaks[i]-breaks[i-1]
        max_len = max(distance,max_len)
    print(max_len)
#4


















