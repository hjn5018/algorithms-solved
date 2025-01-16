import sys
input = sys.stdin.read
data = input().split()

n, m = map(int, data[:2])
nums = sorted(map(int, data[2:]))
visited = [False] * n
result = []
path = []

def backtrack(depth):
    if depth == m:
        result.append(tuple(path))
        return
    
    prev = -1
    for i in range(n):
        if not visited[i] and nums[i] != prev:
            visited[i] = True
            path.append(nums[i])
            backtrack(depth + 1)
            path.pop()
            visited[i] = False
            prev = nums[i]

backtrack(0)

for seq in sorted(set(result)):
    print(*seq)
# https://www.acmicpc.net/status?user_id=hjn5018&problem_id=15663&from_mine=1
