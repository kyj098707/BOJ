n, m = map(int, input().split())
num_list = [0] * (n + 1)


def func(k):
    if k == m:
        for i in range(m):
            print(num_list[i], end=" ")
        print()
        return
    st = 1
    if k != 0:
        st = num_list[k - 1]
    for i in range(st, n + 1):
        num_list[k] = i
        func(k + 1)


func(0)
