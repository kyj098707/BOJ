for _ in range(3):
    tmp = list(map(int, input().split()))
    if tmp.count(1) == 3:
        print("A")
    elif tmp.count(1) == 2:
        print("B")
    elif tmp.count(1) == 1:
        print("C")
    elif tmp.count(1) == 0:
        print("D")
    else:
        print("E")
