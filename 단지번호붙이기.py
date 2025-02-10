from collections import deque

N = int(input())
grid = [list(map(int, input())) for _ in range(N)]

def bfs():
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * N for _ in range(N)]
    sizes = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0 or visited[i][j] == True:
                continue

            visited[i][j] = True
            count = 1
            q = deque([(i, j)])
            
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if grid[nx][ny] == 0 or visited[nx][ny] == True:
                            continue
                        visited[nx][ny] = True
                        count += 1
                        q.append((nx, ny))
            sizes.append(count)

    sizes.sort()
    print(len(sizes))
    for s in sizes:
        print(s)

bfs()
# https://www.acmicpc.net/problem/2667
