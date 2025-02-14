n = int(input())
nums = [int(input()) for _ in range(n)]

if n == 1:
    print(nums[0])  # nums[-1]보다 nums[0]이 직관적
    exit()

if n == 2:
    print(nums[0] + nums[1])  # 두 개만 있는 경우는 바로 합 출력
    exit()

dp = [0] * n  # DP 배열 초기화
dp[0] = nums[0]
dp[1] = nums[0] + nums[1]
dp[2] = max(nums[0] + nums[2], nums[1] + nums[2], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + nums[i], dp[i - 3] + nums[i - 1] + nums[i])

print(dp[-1])

# https://www.acmicpc.net/problem/2156
