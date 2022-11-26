# n개의 하노이가 있을 때 n-1개를 2에, n의 하노이를 3에, 2에서 3으로 가는 n-1를 한번 더
def hanoi(st, en, n):
    if n == 1:
        print(st, en)
        return

    hanoi(st, 6 - st - en, n - 1)
    print(st, en)
    hanoi(6 - st - en, en, n - 1)


n = int(input())
print(2**n - 1)
hanoi(1, 3, n)
