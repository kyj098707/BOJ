n, k = map(int, input().split())
cur_prodcut = [0] * (k + 2)
product_list = list(map(int, input().split()))
multi_tap = []
cnt = 0
for i in range(len(product_list)):

    if cur_prodcut[product_list[i]] == 1:
        continue

    if len(multi_tap) < n:
        multi_tap.append(product_list[i])
        cur_prodcut[product_list[i]] = 1
    else:
        mx_val = 0
        mx_idx = 0
        for j in range(len(multi_tap)):
            try:  # 값이 없을 때 발생
                tmp = product_list[i + 1 :].index(multi_tap[j])
                if mx_val < tmp:
                    mx_val = tmp
                    mx_idx = j

            except:  # 값이 없으면 제거

                mx_idx = j
                break

        cur_prodcut[product_list[i]] = 1
        cur_prodcut[multi_tap[mx_idx]] = 0
        multi_tap[mx_idx] = product_list[i]

        cnt += 1

print(cnt)
