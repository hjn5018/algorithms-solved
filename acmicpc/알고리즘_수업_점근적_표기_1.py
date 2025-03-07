a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

result = 1 if a1 <= c and ((a1 * n0) + a0) <= (c * n0) else 0
print(result)
# https://www.acmicpc.net/problem/24313
