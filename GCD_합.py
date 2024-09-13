def gcd(n: int, m: int) -> int:
    if m > n:
        m, n = n, m
    for i in range(m, 0, -1):
        if n % i == 0 and m % i == 0:
            return i

t = int(input())

for _ in range(t):
    n, *list_ = map(int, input().split())
    sum = 0
    for i in range(n-1):
        for j in range(i+1, n):
            sum += gcd(list_[i], list_[j])
    print(sum)
# https://www.acmicpc.net/problem/9613
