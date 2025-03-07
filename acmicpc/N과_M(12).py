N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
# print(f"{N = }")
# print(f"{M = }")
# print(f"{nums = }")

def permutation(arr:list) -> list:
    result = []
    def dfs(start:int, tmp=[]):
        if len(tmp) == M:
            if tmp not in result:
                result.append(tmp[:])
            return
        for i in range(start, N):
            tmp.append(arr[i])
            dfs(i, tmp)
            tmp.pop()
    dfs(0)
    return result

for p in permutation(nums):
    print(*p)
# https://www.acmicpc.net/problem/15666
