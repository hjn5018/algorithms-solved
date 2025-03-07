from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def find_cc(graph):
    visited = set()  # 방문한 노드를 집합으로 저장
    count = 0

    def bfs(node):
        q = deque([node])  # 큐 초기화
        visited.add(node)  # 방문 표시
        while q:
            a = q.popleft()
            for neighbor in graph.get(a, []):  # 이웃 노드 확인
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)

    for node in graph:
        if node not in visited:
            bfs(node)
            count += 1  # 연결 요소 발견 시 증가
    return count

# 그래프 초기화
graph = {i: [] for i in range(1, N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = find_cc(graph)
print(result)

# https://www.acmicpc.net/problem/11724
