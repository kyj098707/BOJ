D = [0 for _ in range(1002)]

D[1] = 1
D[2] = 3
for i in range(3,1002):
    D[i] = D[i-1] + 2 * D[i-2]

    D[i] %= 10007

n = int(input())
print(D[n])