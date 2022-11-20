import sys

input = sys.stdin.readline

num = int(input())
D = [[0 for _ in range(4)] for __ in range(1003)]
RGB = [[0 for _ in range(4)] for __ in range(1003)]

for i in range(1, num + 1):
    RGB[i][1], RGB[i][2], RGB[i][3] = map(int, input().split())

D[1][1] = RGB[1][1]
D[1][2] = RGB[1][2]
D[1][3] = RGB[1][3]

for i in range(2, 1001):
    D[i][1] = min(D[i - 1][2], D[i - 1][3]) + RGB[i][1]
    D[i][2] = min(D[i - 1][1], D[i - 1][3]) + RGB[i][2]
    D[i][3] = min(D[i - 1][1], D[i - 1][2]) + RGB[i][3]

print(min(min(D[num][1], D[num][2]), D[num][3]))
