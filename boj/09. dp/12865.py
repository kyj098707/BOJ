import sys
input = sys.stdin.readline

n, k = map(int,input().split())
bag = [(0,0)]
knapsack = [[0 for _ in range(k+1)] for __ in range(n+1)]

for _ in range(n):
    bag.append(tuple(map(int, input().split())))

for i in range(1,n+1):
    for j in range(1,k+1):
        w = bag[i][0]
        v = bag[i][1]

        if j < w:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(knapsack[i-1][j-w] + v, knapsack[i-1][j])
print(knapsack[n][k])