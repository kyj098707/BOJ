D = [0] * 1000001

num = int(input())

for i in range(1, num):
    D[i + 1] = D[i] + 1
    if (i + 1) % 2 == 0:
        D[i + 1] = min(D[i + 1], D[(i + 1) // 2] + 1)
    if (i + 1) % 3 == 0:
        D[i + 1] = min(D[i + 1], D[(i + 1) // 3] + 1)


print(D[num])
