n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def permutation(n:int ,m:int):
    result = []
    def dfs(start, tmp=[]):
        if len(tmp) == m and tmp not in result:
            result.append(tmp[:])
            return

        for i in range(start, n):
            tmp.append(nums[i])
            dfs(i + 1, tmp)
            tmp.pop()

    dfs(0)
    return result

result = permutation(n, m)
for r in result:
    print(*r)

# https://www.acmicpc.net/problem/15664
