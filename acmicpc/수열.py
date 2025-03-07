N, K = map(int, input().split())
nums = list(map(int, input().split()))

max_= sum(nums[0:0+K])
tmp = max_
for i in range(N-K):
    tmp -= nums[i]
    tmp += nums[i+K]
    if tmp > max_:
        max_ = tmp

print(max_)
# https://www.acmicpc.net/problem/2559
