N = int(input())
scores = [int(input()) for _ in range(N)]

count = 0
for i in range(len(scores)-1, 0, -1):
    while scores[i] <= scores[i-1]:
        scores[i-1] -= 1
        count += 1
print(count)
# https://www.acmicpc.net/problem/2847
