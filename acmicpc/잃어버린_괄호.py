expr = input()
sub_expr = expr.split("-")

result = 0
for i in range(len(sub_expr)):
    tmp = sub_expr[i].split("+")
    tmp = list(map(int, tmp))
    if i == 0:
        result += sum(tmp)
    else:
        result -= sum(tmp)
print(result)
# https://www.acmicpc.net/problem/1541
