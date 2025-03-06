from collections import deque

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

def bfs(x, y, paper, visited, directions):
    paint_extent = 1
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and paper[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                paint_extent += 1
    return paint_extent

visited = [[False] * m for _ in range(n)]
directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
total_paint = 0
max_paint_extent = 0
for i in range(n):
    for j in range(m):
        if paper[i][j] and not visited[i][j]:
            paint_extent = bfs(i, j, paper, visited, directions)
            max_paint_extent = max(max_paint_extent, paint_extent)
            total_paint += 1
print(total_paint)
print(max_paint_extent)

# https://www.acmicpc.net/problem/1926
