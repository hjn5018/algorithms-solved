n = int(input())
nums = list(map(int, input().split()))

max_sum = float("-inf")
current_sum = 0

for num in nums:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)

print(max_sum)

# https://www.acmicpc.net/problem/1912
