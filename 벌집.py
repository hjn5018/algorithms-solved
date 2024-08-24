N = int(input())
a = 1
b = 1
while True:
    if N <= a:
        break
    else:
        a += 6 * b
        b += 1
print(b)
# https://www.acmicpc.net/problem/2292
