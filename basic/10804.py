card_list = list(range(1,21))

for _ in range(10):
    st, en = map(int, input().split())
    st = st - 1
    en = en - 1
    tmp = card_list[st:en+1]
    card_list[st:en+1] = tmp[::-1]

for card in card_list:
    print(card, end = ' ')