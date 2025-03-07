from collections import deque

N, M = map(int, input().split())
maze = [input() for _ in range(N)]

def bfs(x:int, y:int) -> int:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque([(0, 0, 1)])
    visited = {(0, 0)}
    while q:
        x, y, d = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if maze[nx][ny] == '1':
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append((nx, ny, d + 1))
                        if (nx, ny) == (N - 1, M - 1):
                            print(d + 1)
                            return

bfs(0, 0)
# https://www.acmicpc.net/problem/2178
