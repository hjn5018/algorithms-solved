N = int(input())
M = int(input())
nums = list(map(int, input().split()))

nums.sort(reverse=True)
count = 0
if N == 1:
    print(0)
else:
    if M > nums[0] + nums[1]:
        print(0)
    elif M == nums[0] + nums[1]:
        print(1)
    elif M < nums[0] + nums[1]:
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == M:
                count += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < M:
                right -= 1
            elif nums[left] + nums[right] > M:
                left += 1
        print(count)
# https://www.acmicpc.net/problem/1940
