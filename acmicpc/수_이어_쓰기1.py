N = int(input())
result = 0

l = len(str(N))
result += l * (N - 10**(l-1) + 1)

for i in range(l-1, 0, -1):
    tmp = 9 * 10**(i-1)
    result += tmp * i
print(result)
# https://www.acmicpc.net/problem/1748
