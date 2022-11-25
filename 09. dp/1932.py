import sys

input = sys.stdin.readline
num = int(input())
D = [[0 for _ in range(1003)] for __ in range(1003)]
tri = [[0]]

for _ in range(num):
    tri.append(list(map(int, input().split())))

D[1][0] = tri[1][0]

for i in range(num + 1):
    for j in range(i):
        if j == 0:
            D[i][j] = D[i - 1][j] + tri[i][j]
            continue
        if j == 2 * (i - 1):
            D[i][j] = D[i - 1][j - 1] + tri[i][j]
            continue
        D[i][j] = max(D[i - 1][j - 1] + tri[i][j], D[i - 1][j] + tri[i][j])
print(max(D[num]))
