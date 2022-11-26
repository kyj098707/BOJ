n = int(input())
call_list = list(map(int, input().split()))

y_price = 0
m_price = 0
for i in call_list:
    y_price = y_price + 10 * (int(i / 30) + 1)

    m_price = m_price + 15 * (int(i / 60) + 1)

if y_price < m_price:
    print(f"Y {y_price}")
elif y_price == m_price:
    print(f"Y M {y_price}")
else:
    print(f"M {m_price}")
