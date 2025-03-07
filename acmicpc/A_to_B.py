A, B = map(int, input().split())
i = 0
def dfs(A, B, i):
    if A == B:
        return i + 1
    if A > B:
        return

    # route1
    C = A * 10 + 1
    result = dfs(C, B, i + 1)
    if result is not None:
        return result

    # route2
    D = A * 2
    result = dfs(D, B, i + 1)
    return result

result = dfs(A, B, 0)
print(result if result is not None else -1)
# https://www.acmicpc.net/problem/16953
