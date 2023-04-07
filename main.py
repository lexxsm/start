n = int(input())
s = 3
i = 0
j = 0
for i in range(n):
    for j in range(s, -1,-1):
        if n < 3:
            print("До старта", s, "секунд(ы)")
            s = s - 1
            j = j + 1
            print("Старт", str(n + 1) + "!!!")
        i = i + 1
        break
