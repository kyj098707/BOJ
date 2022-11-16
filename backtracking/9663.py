n = int(input())
cnt = 0
is_used1 = [0] * (n + 2)
is_used2 = [0] * (2 * n + 2)
is_used3 = [0] * (2 * n + 2)


def Q(col):
    global cnt
    if col == n:
        cnt += 1
        return
    else:
        for i in range(n):
            if is_used1[i] or is_used2[col + i] or is_used3[col - i + n - 1]:
                continue
            is_used1[i] = 1
            is_used2[col + i] = 1
            is_used3[col - i + n - 1] = 1
            Q(col + 1)
            is_used1[i] = 0
            is_used2[col + i] = 0
            is_used3[col - i + n - 1] = 0


Q(0)
print(cnt)
