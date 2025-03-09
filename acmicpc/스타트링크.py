from collections import deque

# 1 <= S, G <= F <= 1_000_000, 0 <= U, D <= 1_000_000
F, S, G, U, D = map(int, input().split())

def bfs(F, S, G, U, D):
    queue = deque([(S, 0)])
    visited = set([S])
    while queue:
        current_floor, count = queue.popleft()
        
        if current_floor == G:
            return count
        
        for dx in [U, -D]:
            nx = current_floor + dx
            if 1 <= nx <= F and nx not in visited:
                queue.append((nx, count + 1))
                visited.add(nx)

    return "use the stairs"  # 도달 불가능한 경우


print(bfs(F, S, G, U, D))

# https://www.acmicpc.net/problem/5014
