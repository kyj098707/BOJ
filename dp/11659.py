import sys

input = sys.stdin.readline

n, m = map(int, input().split())
D = [0] * 100003
num_list = list(map(int, input().split()))
D[1] = num_list[0]

for i in range(2, n + 1):
    D[i] = D[i - 1] + num_list[i - 1]

for _ in range(m):
    a, b = map(int, input().split())
    print(D[b] - D[a - 1])
