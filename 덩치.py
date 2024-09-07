N = int(input())

people = [list(map(int, input().split())) for _ in range(N)]

result = []
for i in people:
    count = 0
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            count += 1
    result.append(count + 1)

print(*result)
# https://www.acmicpc.net/problem/7568
