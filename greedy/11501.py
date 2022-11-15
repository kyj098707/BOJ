import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    num = int(input())
    price_list = []

    price_list = list(map(int, input().split()))
    stack = [0]
    buy = []
    for price in price_list[::-1]:
        if price > stack[-1]:
            buy.append(0)
            stack.append(price)
        else:
            buy.append(stack[-1])
    total = 0

    for price in price_list:
        if buy[-1]:
            total += buy.pop() - price
        else:
            buy.pop()

    print(total)
