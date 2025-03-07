from collections import deque

N = int(input())
graph_ = [list(map(int, input().split())) for _ in range(N)]
graph = {i:[] for i in range(1, N + 1)}
for i in range(N):
    for j in range(N):
        if graph_[i][j] == 1:
            graph[i + 1].append(j + 1)

def is_connected(s:int, e:int) -> bool:
    visited = [False] * (N + 1)
    q = deque(graph[s])
    visited[s] = True
    while q:
        x = q.popleft()
        if x == e:
            return True
        if visited[x]:
            continue
        q.extend(graph[x])
        visited[x] = True
    return False

arr = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if is_connected(i + 1, j + 1):
            arr[i][j] = 1

for i in arr:
    print(*i)
# https://www.acmicpc.net/problem/history/11403
