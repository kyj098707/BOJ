num = int(input())
stair_list = [0] * (305)

for i in range(1, num + 1):
    stair_list[i] = int(input())


D = [[0 for _ in range(3)] for __ in range(305)]

D[1][1] = stair_list[1]
D[1][0] = stair_list[0]
D[2][1] = stair_list[2]
D[2][2] = stair_list[1] + stair_list[2]
if i != 1:
    for i in range(3, num + 1):
        D[i][1] = max(D[i - 2][2], D[i - 2][1]) + stair_list[i]
        D[i][2] = D[i - 1][1] + stair_list[i]

print(max(D[num][1], D[num][2]))
