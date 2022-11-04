import math

n, k = map(int, input().split())
room_cnt = 0
student_list = [0] * 13
for i in range(n):
    gender, age = map(int, input().split())
    student_list[gender * 6 + age] = student_list[gender * 6 + age] + 1 

for student_num in student_list:
    room_cnt = room_cnt + math.ceil(student_num/k)


print(room_cnt)