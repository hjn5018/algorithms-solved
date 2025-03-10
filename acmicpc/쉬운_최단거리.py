from collections import deque

n, m = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(n)]

def find_start(n, m, _map):
    for i in range(n):
        for j in range(m):
            if _map[i][j] == 2:
                return (i, j)
            

def bfs(start, n, m, _map, visited, result):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([(*start, 0)])
    visited[start[0]][start[1]] = True
    _map[start[0]][start[1]] = 0
    while queue:
        x, y, count = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and _map[nx][ny] == 1 and not visited[nx][ny]:
                result[nx][ny] = count + 1
                queue.append((nx, ny, count + 1))
                visited[nx][ny] = True


def solve():
    start = find_start(n, m, _map)
    visited = [[False] * m for _ in range(n)]
    result = [[0] * m for _ in range(n)]
    bfs(start, n, m, _map, visited, result)
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and _map[i][j] == 1:
                result[i][j] = -1
    for k in result:
        print(*k)

solve()

# https://www.acmicpc.net/problem/14940
