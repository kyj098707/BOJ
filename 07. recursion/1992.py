num = int(input())
quad_tree = []

for _ in range(num):
    quad_tree.append(list(map(int, " ".join(input()).split())))


def func(st_x, st_y, n):
    base_num = quad_tree[st_x][st_y]
    for i in range(st_x, st_x + n):
        for j in range(st_y, st_y + n):
            if base_num != quad_tree[i][j]:
                print("(", end="")
                func(st_x, st_y, n // 2)
                func(st_x, st_y + n // 2, n // 2)
                func(st_x + n // 2, st_y, n // 2)
                func(st_x + n // 2, st_y + n // 2, n // 2)
                print(")", end="")
                return
    print(base_num, end="")


func(0, 0, num)
