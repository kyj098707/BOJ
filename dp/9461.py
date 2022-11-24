D = [0] * 103
D[1] = 1
D[2] = 1
D[3] = 1
D[4] = 2
D[5] = 2

for i in range(6, 101):
    D[i] = D[i - 1] + D[i - 5]

n = int(input())
for _ in range(n):
    print(D[int(input())])
