from collections import deque, defaultdict

# 입력
N, M = map(int, input().split()) # 2 <= N <= 100, 1 <= M <= 5,000

graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

min_num = 100
min_bacon = float("inf")

def bfs(x:int) -> int:
    bacon_num = 0
    visited = [False] * (N + 1)
    q = deque([(x, 0)])
    visited[x] = True
    while q:
        a, b = q.popleft()
        for j in graph[a]:
            if not visited[j]:
                q.append((j, b + 1))
                visited[j] = True
                bacon_num += b + 1
    return bacon_num

for i in range(1, N + 1):
    bacon_num = bfs(i)
    if min_bacon > bacon_num:
        min_num = i
        min_bacon = bacon_num


# 출력
print(min_num)

# https://www.acmicpc.net/problem/1389
