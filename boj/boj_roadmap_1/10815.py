n = int(input())
num_list = sorted(list(map(int, input().split())))

tgt_n = int(input())
tgt_list = list(map(int, input().split()))


def bs(tgt):
    st = 0
    en = n - 1

    while st <= en:
        mid = (st + en) // 2
        if num_list[mid] == tgt:
            print(1, end=" ")
            return
        if num_list[mid] > tgt:
            en = mid - 1
        else:
            st = mid + 1

    print(0, end=" ")
    return


for tgt in tgt_list:
    bs(tgt)
