import sys

input = sys.stdin.readline

n = int(input())
p = []
for _ in range(n):
    p.append(int(input().rstrip()))
if n == 1:
    print(p[0])
    exit()
dp = [[0, 0, 0] for _ in range(n)]
for i in range(n):
    dp[i][0] = dp[i - 1][2] + p[i]
    dp[i][1] = dp[i - 1][0] + p[i]
    dp[i][2] = max(dp[i - 1][1], dp[i - 1][0], dp[i - 1][2])

print(max(dp[n - 1]))
