N = input()
N = int(N)

def rec(N):
    if N == 1:
        return 1
    if N == 0:
        return 1
    return rec(N-1) * N

print(rec(N))
# https://www.acmicpc.net/problem/27433
