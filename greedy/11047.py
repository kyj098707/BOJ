import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin_list = []
for _ in range(n):
    coin_list.append(int(input()))
total = 0
cnt = 0
index = n-1

while total != k:
    if total + coin_list[index] <= k:
        total += coin_list[index]
        cnt += 1
    else:
        index -= 1

print(cnt)