from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))

operator_nums = list(map(int, input().split()))
OPERATORS = ['+', '-', '*', '/']
operators = []
for i in range(len(operator_nums)):
    for _ in range(operator_nums[i]):
        operators.append(OPERATORS[i])

max_ = float("-inf")
min_ = float("inf")
perm = list(set(permutations(operators)))

for i in range(len(perm)):
    result = nums[0]
    for j in range(N - 1):
        if perm[i][j] == '+':
            result += nums[j + 1]
        elif perm[i][j] == '-':
            result -= nums[j + 1]
        elif perm[i][j] == '*':
            result *= nums[j + 1]
        elif perm[i][j] == '/':
            if result < 0:
                result *= -1
                result //= nums[j + 1]
                result *= -1
            else:
                result //= nums[j + 1]
        
    if max_ < result:
        max_ = result
    if min_ > result:
        min_ = result
print(max_)
print(min_)
# https://www.acmicpc.net/problem/14888
