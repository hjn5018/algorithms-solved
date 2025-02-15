def solve(N: int) -> int:
    MOD = 1_000_000_000
    
    # dp[i][j] = 길이가 i인 숫자 중 끝 자리가 j인 경우의 개수
    dp = [[0] * 10 for _ in range(N + 1)]
    
    # 첫 번째 자리는 1부터 9까지 각 자리에 대해 1개씩 시작할 수 있다.
    for i in range(1, 10):
        dp[1][i] = 1
    
    # DP 테이블 채우기
    for i in range(2, N + 1):
        for j in range(10):
            if j - 1 >= 0:
                dp[i][j] += dp[i - 1][j - 1]
            if j + 1 <= 9:
                dp[i][j] += dp[i - 1][j + 1]
            dp[i][j] %= MOD
    
    # 결과는 길이가 N인 숫자에서 가능한 끝 자리를 모두 더한 값
    result = sum(dp[N]) % MOD
    return result

N = int(input())

result = solve(N) % 1_000_000_000
print(result)

# https://www.acmicpc.net/problem/10844
