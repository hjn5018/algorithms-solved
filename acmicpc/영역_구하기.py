from collections import deque

def get_paper(M:int, N:int) -> list:
    paper = [[0] * N for _ in range(M)]
    return paper

def paint_paper(square:list, paper:list):
    sx, sy, ex, ey = square
    for x in range(sx, ex):
        for y in range(sy, ey):
            paper[y][x] = 1
    return

def bfs(x:int, y:int, visited:list, areas:list, paper:list):
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    q = deque()
    q.append((x, y))
    visited[y][x] = 1
    area = 1
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[ny][nx] and paper[ny][nx] != 1:
                    visited[ny][nx] = 1
                    q.append((nx, ny))
                    area += 1
    areas.append(area)
    return

def get_isolated_areas(paper:list):
    areas = []
    visited = [[False] * N for _ in range(M)]
    for x in range(N):
        for y in range(M):
            if paper[y][x] == 0 and not visited[y][x]:
                bfs(x, y, visited, areas, paper)
    return areas


def solve(M:int, N:int, squares:list):
    paper = get_paper(M, N)

    for square in squares:
        paint_paper(square, paper)

    areas = get_isolated_areas(paper)
    print(len(areas))
    print(*sorted(areas))
    return

# 입력
M, N, K = map(int, input().split())
squares = [list(map(int, input().split())) for _ in range(K)]

solve(M, N, squares)
# https://www.acmicpc.net/problem/2583
