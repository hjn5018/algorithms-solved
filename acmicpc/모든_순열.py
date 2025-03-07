from itertools import permutations

N = int(input())

for i in permutations(range(1, N+1), N):
    print(*i)
# https://www.acmicpc.net/problem/10974
