n = int(input())
a = list(map(int, input().split()))

# DP 배열 초기화
dp = [1] * len(a)

# DP 계산
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:  # 증가하는 조건
            dp[i] = max(dp[i], dp[j] + 1)

# 결과 출력
print(max(dp))

# https://www.acmicpc.net/problem/1965
