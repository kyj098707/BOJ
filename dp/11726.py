n = int(input())

D = [0] * 1003
D[1] = 1
D[2] = 2


for i in range(3, 1003):
    D[i] = D[i - 2] + D[i - 1]
    D[i] %= 10007

print(D[n])
