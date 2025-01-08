from collections import defaultdict

n = int(input())
x, y = map(int, input().split())
m = int(input())

graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def search():
    visited = [False] * (n + 1)
    visited[x] = True

    def dfs(start, num):
        for node in graph[start]:
            if not visited[node]:
                visited[node] = True
                if node == y:
                    return num  # 목표 노드에 도달했으면 거리 반환
                result = dfs(node, num + 1)  # 다음 노드로 이동
                if result is not None:  # 하위 호출에서 결과가 반환되면 그대로 전달
                    return result
        return None  # 목표 노드에 도달하지 못하면 None 반환

    result = dfs(x, 1)
    return result if result is not None else -1  # 결과가 None이면 -1 반환

print(search())

# https://www.acmicpc.net/problem/2644
