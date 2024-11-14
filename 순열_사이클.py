T = int(input())
for _ in range(T):
    N = int(input())
    permutation = list(map(int, input().split()))

    loop_count = 0
    visited = set()
    for start in range(1, N + 1):
        if start not in visited:
            current = start
            while current not in visited:
                visited.add(current)
                current = permutation[current - 1]  # 0-based index 접근
            loop_count += 1  # 사이클을 완성하면 사이클 개수 증가

    print(loop_count)

# https://www.acmicpc.net/problem/10451
