n, m = map(int, input().split())

num_list = sorted(list(map(int, input().split())))
is_used = [0] * (10000 + 1)
result_list = [0] * (m + 1)


def func(k):
    if k == m:
        for i in range(m):
            print(result_list[i], end=" ")
        print()
        return
    tmp = 0

    for i in range(n):
        if is_used[i] == 1:
            continue
        if num_list[i] == tmp:
            continue

        is_used[i] = 1
        tmp = num_list[i]
        result_list[k] = num_list[i]

        func(k + 1)
        is_used[i] = 0


func(0)
