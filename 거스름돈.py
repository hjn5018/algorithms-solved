n = int(input())

def optimize(n: int) -> int:
    if (n % 5) % 2 == 0:
        return (n // 5) + ((n % 5) // 2)
    return ((n // 5) - 1) + (((n % 5) + 5) // 2)

if n in [1, 3]:
    print(-1)
elif n % 5 == 0:
    print(n // 5)
else:
    print(optimize(n))
# https://www.acmicpc.net/problem/14916
