n, m = map(int, input().split())

num_list = [0] * (n + 1)


def func(k):
    if k == m:
        for i in range(m):
            print(num_list[i], end=" ")
        print()
        return
    for i in range(1, n + 1):
        num_list[k] = i
        func(k + 1)


func(0)
