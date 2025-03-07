def count_factors(n, factor):
    count = 0
    while n >= factor:
        count += n // factor
        n //= factor
    return count

def trailing_zeros(n, m):
    count_2 = count_factors(n, 2) - count_factors(m, 2) - count_factors(n - m, 2)
    count_5 = count_factors(n, 5) - count_factors(m, 5) - count_factors(n - m, 5)
    return min(count_2, count_5)

# 입력
n, m = map(int, input().split())
print(trailing_zeros(n, m))

# https://www.acmicpc.net/problem/2004
