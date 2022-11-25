D = [[0 for _ in range(2)] for __ in range(1000003)]

D[1][0] = 0
D[1][1] = 0
D[2][0] = 1
D[2][1] = 1
for i in range(2, 1000001):
    D[i + 1][0] = D[i][0] + 1
    D[i + 1][1] = i
    if (i + 1) % 2 == 0 and D[i + 1][0] > D[(i + 1) // 2][0] + 1:
        D[i + 1][0] = D[(i + 1) // 2][0] + 1
        D[i + 1][1] = (i + 1) // 2
    if (i + 1) % 3 == 0 and D[i + 1][0] > D[(i + 1) // 3][0] + 1:
        D[i + 1][0] = D[(i + 1) // 3][0] + 1
        D[i + 1][1] = (i + 1) // 3
num = int(input())
print(D[num][0])
tmp = D[num]
print(num, end=" ")
while tmp[1]:
    print(tmp[1], end=" ")
    tmp = D[tmp[1]]
print()
