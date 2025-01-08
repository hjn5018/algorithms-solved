from collections import defaultdict, deque

n = int(input())
x, y = map(int, input().split())
m = int(input())

graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(f"{graph = }")

def bfs():
    visited = [False] * (n + 1)
    visited[x] = True
    q = deque([(x, 0)])

    while q:
        current, num = q.popleft()
        if current == y:
            return num
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append([neighbor, num + 1])
    return -1

print(bfs())
# https://www.acmicpc.net/problem/2644
