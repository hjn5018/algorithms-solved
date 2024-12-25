from collections import defaultdict, deque
import sys

input = sys.stdin.readline

# 입력 처리
n = int(input())  # 노드의 개수
graph = defaultdict(list)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 부모를 저장할 리스트
parents = [0] * (n + 1)

# BFS를 사용하여 부모 찾기
def find_parents():
    queue = deque([1])  # 루트 노드 1부터 시작
    visited = [False] * (n + 1)
    visited[1] = True  # 루트는 방문 처리

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                parents[neighbor] = current  # 부모 기록
                visited[neighbor] = True
                queue.append(neighbor)

find_parents()

# 결과 출력
for i in range(2, n + 1):
    print(parents[i])

# https://www.acmicpc.net/problem/11725
