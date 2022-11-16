n, m = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
result_list = [0] * (n + 1)


def func(k):
    if k == m:
        for i in range(m):
            print(result_list[i], end=" ")
        print()
        return
    for i in range(1, n + 1):

        result_list[k] = num_list[i - 1]
        func(k + 1)


func(0)
