equation = input()
equation_num = "+".join(equation.split("-")).split("+")

op_list = []

for c in equation:
    if c == "-" or c == "+":
        op_list.append(c)
for i in range(1, len(op_list)):
    if op_list[i] == "+" and op_list[i - 1] == "-":
        op_list[i] = "-"
total = 0
for i in range(len(equation_num)):
    if i == 0:
        total = total + int(equation_num[i])
        continue
    if op_list[i - 1] == "+":
        total = total + int(equation_num[i])
    else:
        total = total - int(equation_num[i])

print(total)
