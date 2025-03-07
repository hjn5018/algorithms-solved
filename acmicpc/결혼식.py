n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

depth = 0
guests = set()
def dfs(node:int):
    global depth
    depth += 1
    if depth > 2:
        return
    for next_node in graph[node]:
        guests.add(next_node)
        dfs(next_node)
        depth -= 1

dfs(1)

if guests:
    result = len(guests) - 1
else:
    result = 0

print(result)
# https://www.acmicpc.net/problem/5567
