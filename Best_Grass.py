from collections import deque

R, C = map(int, input().split())

pasture = [input() for i in range(R)]
visited = [[False] * C for _ in range(R)]
count = 0
def bfs(i:int, j:int):
    global count
    visited[i][j] = True
    queue = deque([[i, j]])
    directions = [[0, 1], [1, 0]]
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C and not visited[ny][nx] and pasture[ny][nx] == '#':
                visited[ny][nx] = True
                queue.append([ny, nx])
    count += 1

for i in range(R):
    for j in range(C):
        if visited[i][j] == False and pasture[i][j] == '#':
            bfs(i, j)

print(count)
# https://www.acmicpc.net/problem/6186
