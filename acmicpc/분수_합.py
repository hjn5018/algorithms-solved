def gcd(a:int, b:int) -> int:
    while b:
        a, b = b, a%b
    return a

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

b3 = b1 * b2
a3 = b2 * a1 + b1 * a2

c = gcd(a3, b3)
b3 = int(b3 / c)
a3 = int(a3 / c)

print(a3, b3)
# https://www.acmicpc.net/problem/1735
