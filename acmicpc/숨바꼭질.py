from collections import deque

N, K = map(int, input().split())

visited = [-1] * 100_001
q = deque([N])
visited[N] = 0

def bfs():
    while q:
        position = q.popleft()

        if position == K:
            return visited[position]

        for i in (position-1, position+1, 2*position):
            if 0 <= i <= 100_000 and visited[i] == -1:
                visited[i] = visited[position] + 1
                q.append(i)

print(bfs())

# https://www.acmicpc.net/problem/1697
