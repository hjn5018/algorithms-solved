from collections import defaultdict, deque
import sys

input = sys.stdin.readline

# 입력 받기
N, M, K, X = map(int, input().split())

# 그래프 초기화
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# BFS를 이용한 최단 거리 계산
visited = [-1] * (N + 1)  # 방문 여부와 거리 기록 (-1로 초기화)
visited[X] = 0            # 시작점의 거리는 0
queue = deque([X])        # BFS 큐

while queue:
    current = queue.popleft()
    for neighbor in graph[current]:
        if visited[neighbor] == -1:  # 방문하지 않은 도시
            visited[neighbor] = visited[current] + 1
            queue.append(neighbor)

# 거리 K인 도시 찾기
result = [i for i in range(1, N + 1) if visited[i] == K]

# 결과 출력
if result:
    print("\n".join(map(str, sorted(result))))
else:
    print(-1)

# https://www.acmicpc.net/problem/18352
