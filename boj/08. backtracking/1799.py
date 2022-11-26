n = int(input())

board = []
is_used1 = [0] * 30
is_used2 = [0] * 30
for _ in range(n):
    board.append(list(map(int, input().split())))
cnt = 0


def bishop(row):
    global cnt
    if row == n:
        cnt += 1
        return

    for i in range(n):
        if (
            is_used1[row + i] == 1
            or is_used2[row - i + n - 1] == 1
            or board[row][i] == 0
        ):
            continue

        is_used1[row + i] = 1
        is_used2[row - i + n - 1] = 1
        bishop(row + 1)
        is_used1[row + i] = 0
        is_used2[row - i + n - 1] = 0


bishop(0)
print(cnt)
