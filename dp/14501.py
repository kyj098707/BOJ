import sys

input = sys.stdin.readline

num = int(input())

sche = []
for _ in range(num):
    day, charge = map(int, input().split())
    sche.append([day, charge])
D = [0 for _ in range(1500002)]

mx = 0
for i in range(1, num + 1):
    for j in range(i):
        if j + sche[j][0] > i:
            continue
        D[i] = max(D[j] + sche[j][1], D[i])

    mx = max(D[i], mx)

print(mx)
