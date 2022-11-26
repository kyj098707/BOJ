visit = [0 for _ in range(10000003)]
def solution(k, tangerine):
    answer = 0
    for i in range(len(tangerine)):
        visit[tangerine[i]] += 1
    n_list = []
    for i in range(10000003):
        if visit[i] != 0:
            n_list.append(visit[i])
    n_list.sort()
    while k > 0 and len(n_list):
        k -= n_list[-1]
        n_list.pop()
        answer += 1
    return answer