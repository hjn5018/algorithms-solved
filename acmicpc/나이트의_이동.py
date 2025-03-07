from collections import deque

def solve(n:int):
    arr = [[False] * n for _ in range(n)]
    cx, cy = map(int, input().split())
    tx, ty = map(int, input().split())
    if (cx, cy) == (tx, ty):
        return 0
    arr[tx][ty] = True
    visited = [[False] * n for _ in range(n)]
    directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    q = deque()
    q.append((cx, cy, 0))
    visited[cx][cy] = True
    while q:
        x, y, c = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if (nx, ny) == (tx, ty):
                    return c + 1
                
                if not visited[nx][ny]:
                    q.append((nx, ny, c + 1))
                    visited[nx][ny] = True

for _ in range(int(input())):
    result = solve(int(input()))
    print(result)
# https://www.acmicpc.net/problem/7562
