N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_ = prices[0]
result = 0
i = 0
while i < N-1:
    result += min_ * distances[i]
    i += 1
    if min_ > prices[i]:
        min_ = prices[i]

print(result)
# https://www.acmicpc.net/problem/13305
