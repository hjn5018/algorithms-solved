N, M = map(int, input().split())

potentials = [int(input()) for _ in range(M)]

set_ = set(potentials)
potentials.sort(reverse=True)
max_sales = 0
sales = []
for i in set_:
    tmp_sales = 0
    counter = 0
    for j in potentials:
        if j >= i and counter < N:
            tmp_sales += i
            counter += 1
    sales.append((i, tmp_sales))

sales.sort(key=lambda x: (-x[1], x[0]))
print(*sales[0])
# https://www.acmicpc.net/problem/1246
