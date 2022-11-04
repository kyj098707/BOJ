_, X = map(int, input().split())

input_list = list(map(int, input().split()))

for num in input_list:

    if X > num:
        print(num, end=" ")
