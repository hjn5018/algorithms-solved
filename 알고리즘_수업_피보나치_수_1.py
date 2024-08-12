N = int(input())
n1, n2 = 0, 0

def fib(N):
    global n1
    if N == 1 or N == 2:
        n1 += 1
        return 1
    return fib(N-1) + fib(N-2)

def fibonacci(N):
    global n2
    a, b = 1, 1
    for _ in range(3, N+1):
        a, b = b, a+b
        n2 += 1
    return a

fib(N)
fibonacci(N)
print(n1, n2)
# https://www.acmicpc.net/problem/24416
