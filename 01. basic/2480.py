dice_list = sorted(list(map(int, input().split())))

### 3개다 같은 경우
if dice_list[0] == dice_list[2]:
    price = 10000 + 1000 * dice_list[0]
elif dice_list[0] == dice_list[1]:
    price = 1000 + 100 * dice_list[0]
elif dice_list[1] == dice_list[2]:
    price = 1000 + 100 * dice_list[1]
else:
    price = 100 * dice_list[2]

print(price)
