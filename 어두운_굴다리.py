N = int(input())
M = int(input())
x = list(map(int, input().split()))

diff = 0
for i in range(len(x)-1):
    if (x[i+1] - x[i]) % 2 == 0:
        if diff < (x[i+1] - x[i])//2:
            diff = (x[i+1] - x[i])//2
    elif (x[i+1] - x[i]) % 2 != 0:
        if diff < (x[i+1] - x[i])//2 + 1:
            diff = (x[i+1] - x[i])//2 + 1

max_diff = max(x[0], diff, N-x[-1])
print(max_diff)
# https://www.acmicpc.net/problem/17266
