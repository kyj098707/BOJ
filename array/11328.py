it = int(input())

for _ in range(it):
    tmp = [0] * 27
    tmp2 = [0] * 27

    a, b = input().split()
    if len(a) != len(b):
        print("Impossible")
        continue
    for c_a, c_b in zip(a,b):
        tmp[ord(c_a) - ord('a')] = tmp[ord(c_a) - ord('a')] + 1
        tmp2[ord(c_b) - ord('a')] = tmp2[ord(c_b) - ord('a')] + 1

    if tmp==tmp2:
        print("Possible")
    else:
        print("Impossible")