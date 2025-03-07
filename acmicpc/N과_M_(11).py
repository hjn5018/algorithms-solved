n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def permutation(n, m):
    result = set()  # 중복을 없애기 위한 set 사용
    def dfs(tmp=[]):
        if len(tmp) == m:
            result.add(tuple(tmp))  # 리스트를 튜플로 변환하여 set에 추가
            return

        for i in range(n):
            tmp.append(nums[i])
            dfs(tmp)
            tmp.pop()

    dfs()
    return result

result = permutation(n, m)
for r in sorted(result):  # 출력 시 정렬
    print(*r)
# https://www.acmicpc.net/problem/15665
