import sys
input = sys.stdin.readline
N = int(input())

line_list = []
for _ in range(N):
    line_st, line_en = map(int, input().split())
    line_list.append((line_st, line_en))

line_list.sort(key=lambda x:x[0])

result_stack = [(-1000000001,-1000000001)]
total = 0
for line in line_list:
    if line[0] > result_stack[-1][1]:
        total += result_stack[-1][1] - result_stack[-1][0]
        result_stack.pop()
        result_stack.append(line)
    
    else:
        tmp_st = result_stack[-1][0]
        tmp_en = max(line[1],result_stack[-1][1])
        result_stack.pop()
        result_stack.append((tmp_st,tmp_en))
while result_stack:
    total += result_stack[-1][1] - result_stack[-1][0]
    result_stack.pop()
print(total)