L, C = map(int, input().split())

passw_list = sorted(list(input().split()))
result = ["0"] * L
is_used = [0] * 30


def func(k, st):
    if k == L:
        if (
            is_used[0]
            + is_used[ord("e") - ord("a")]
            + is_used[ord("i") - ord("a")]
            + is_used[ord("o") - ord("a")]
            + is_used[ord("u") - ord("a")]
            < 1
        ):
            return
        if (
            is_used[0]
            + is_used[ord("e") - ord("a")]
            + is_used[ord("i") - ord("a")]
            + is_used[ord("o") - ord("a")]
            + is_used[ord("u") - ord("a")]
            > L - 2
        ):
            return
        for i in range(L):
            print(result[i], end="")
        print()
        return

    for i in range(st, C):
        result[k] = passw_list[i]
        is_used[ord(passw_list[i]) - ord("a")] = 1
        func(k + 1, i + 1)
        is_used[ord(passw_list[i]) - ord("a")] = 0


func(0, 0)
