N = int(input())
first, *nums = map(int, input().split())

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

for i in nums:
    g = gcd(first, i)
    result = f"{first//g}/{i//g}"
    print(result)
# https://www.acmicpc.net/problem/3036
