n = int(input())
paper_list = []
color_list = [0 for _ in range(2)]
for _ in range(n):
    paper_list.append(list(map(int, input().split())))


def func(st_x, st_y, n):
    color = paper_list[st_x][st_y]
    for i in range(st_x, st_x + n):
        for j in range(st_y, st_y + n):
            if paper_list[i][j] != color:
                func(st_x, st_y, n // 2)
                func(st_x + n // 2, st_y, n // 2)
                func(st_x, st_y + n // 2, n // 2)
                func(st_x + n // 2, st_y + n // 2, n // 2)
                return

    color_list[color] += 1


func(0, 0, n)
for color in color_list:
    print(color)
