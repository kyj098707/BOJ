import sys
input = sys.stdin.readline

n, k = map(int, input().split())
money_list = []
for _ in range(n):
    money_list.append(int(input()))
D = [0 for _ in range(10003)]



for i in range(n):
    if money_list[i] > k+1:
        continue
    D[money_list[i]] += 1
    for j in range(money_list[i],k+1):

        D[j] += D[j-money_list[i]]

print(D[k])