n, m = map(int, input().split())
num_list = sorted(list(map(int, input().split())))

result_list = [0] * (m + 1)
is_used = [0] * 10001


def func(k):
    if k == m:
        for i in range(m):
            print(result_list[i], end=" ")
        print()
        return

    for num in num_list:
        if is_used[num]:
            continue
        result_list[k] = num
        is_used[num] = 1
        func(k + 1)
        is_used[num] = 0


func(0)
