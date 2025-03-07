N = input()
N = int(N)

def fibonacci(N):
    if N < 2:
        return N
    return fibonacci(N-2) + fibonacci(N-1)

print(fibonacci(N))
# https://www.acmicpc.net/problem/10870
