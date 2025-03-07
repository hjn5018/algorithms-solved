def is_prime(n: int) -> bool:
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True

test_cases = [int(input()) for _ in range(int(input()))]

for n in test_cases:
    while not is_prime(n):
        n += 1
    print(n)
# https://www.acmicpc.net/problem/4134
