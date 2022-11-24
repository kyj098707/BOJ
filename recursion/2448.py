n = int(input())

stars = [[" " for _ in range(n * 2)] for __ in range(n)]


def func(st_x, st_y, N):
    if N == 3:  ## st_x, st_y 는 머리 꼭대기 기준
        stars[st_x][st_y] = "*"
        stars[st_x + 1][st_y - 1] = "*"
        stars[st_x + 1][st_y + 1] = "*"
        stars[st_x + 2][st_y - 2] = "*"
        stars[st_x + 2][st_y - 1] = "*"
        stars[st_x + 2][st_y] = "*"
        stars[st_x + 2][st_y + 1] = "*"
        stars[st_x + 2][st_y + 2] = "*"

        return

    func(st_x, st_y, N // 2)
    func(st_x + N // 2, st_y - N // 2, N // 2)
    func(st_x + N // 2, st_y + N // 2, N // 2)


func(0, n - 1, n)

for star in stars:
    print("".join(star))
