N, K = map(int, input().split())
people = [i + 1 for i in range(N)]
removed = []

idx = 0
while people:
    idx += K - 1
    while idx >= len(people):
        idx -= len(people)
    removed.append(people.pop(idx))

removed = ', '.join(map(str, removed))
print(f"<{removed}>")

# https://www.acmicpc.net/problem/11866
