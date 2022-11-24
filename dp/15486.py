import sys

input = sys.stdin.readline

num = int(input())
D = [0 for _ in range(1501003)]

sche = []
for _ in range(num):
    day, charge = map(int, input().split())
    sche.append((day, charge))

D[0] = 0

mx = 0
for i in range(num):
    mx = max(D[i], mx)
    D[i + sche[i][0]] = max(D[i + sche[i][0]], mx + sche[i][1])

mx = max(D[num], mx)
print(mx)
