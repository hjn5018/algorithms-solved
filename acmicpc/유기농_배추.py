from collections import deque
import sys
input = sys.stdin.readline

def bfs(patch, i, j, directions, visited):
    queue = deque([(i, j)])
    visited.add((i, j))
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if patch[nx][ny] == 1 and (nx, ny) not in visited:
                    queue.append([nx, ny])
                    visited.add((nx, ny))

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    patch = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        patch[y][x] = 1

    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    visited = set()
    count = 0
    for i in range(N):
        for j in range(M):
            if patch[i][j] == 1:
                if (i, j) not in visited:
                    bfs(patch, i, j, directions, visited)
                    count += 1
    print(count)

# https://www.acmicpc.net/problem/1012
