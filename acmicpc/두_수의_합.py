n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums = list(filter(lambda a: a < x, nums))
nums.sort()

left, right = 0, len(nums)-1
count = 0
while left < right:
    sum_ = nums[left] + nums[right]
    if sum_ == x:
        count += 1
        right -= 1
        left += 1
    elif sum_ > x:
        right -= 1
    elif sum_ < x:
        left += 1

print(count)
# https://www.acmicpc.net/problem/3273
