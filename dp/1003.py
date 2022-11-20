D = [[0 for __ in range(2)] for _ in range(42)]
D[0][0] = 1
D[0][1] = 0
D[1][0] = 0
D[1][1] = 1

for i in range(2, 42):
    D[i][0] = D[i - 1][0] + D[i - 2][0]
    D[i][1] = D[i - 1][1] + D[i - 2][1]

T = int(input())
for _ in range(T):
    result = D[int(input())]
    print(result[0], result[1])
