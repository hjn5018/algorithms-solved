import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = {i:[] for i in range(1, N + 1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

visited = [0] * (N + 1)
order = 1
def dfs(node:int):
    global order
    visited[node] = order

    for next_node in graph[node]:
        if visited[next_node] == 0:
            order += 1
            dfs(next_node)
    return

dfs(R)

for i in range(1, N + 1):
    print(visited[i])
# https://www.acmicpc.net/problem/24479
