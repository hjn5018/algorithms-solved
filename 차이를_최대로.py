from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))

def sum_abs(arr:list) -> int:
    result = 0
    for i in range(N-1):
        result += abs(arr[i] - arr[i+1])
    return result

result = 0
for p in permutations(nums, N):
    result = max(result, sum_abs(p))
print(result)
# https://www.acmicpc.net/problem/10819
