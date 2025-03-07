N = int(input())

# 4번 코드: 통과
def dp(N:int) -> int:
    if N == 1:
        return 1
    if N == 2:
        return 2
    
    dp = [0] * (N+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N+1):
        dp[i] = (dp[i-1] % 15746 + dp[i-2] % 15746) % 15746
    return dp[N]
print(dp(N))

# 3번 코드: 시간 초과
# a, b = 1, 2
# for _ in range(3, N+1):
#     a, b = b, a + b
# print(b)

# 2번 코드: 메모리 초과
# def dp(N:int) -> int:
#     dp = [0] * (N+1)

#     dp[1] = 1
#     dp[2] = 2
#     for i in range(3, N+1):
#         dp[i] = dp[i-1] + dp[i-2]
#     return dp[N]
# print(dp(N))

# 1번 코드 recursion error
# def f(N:int) -> int:
#     if N == 1:
#         return 1
#     if N == 2:
#         return 2
#     return f(N-1) + f(N-2)
# print(f(N)) 

# https://www.acmicpc.net/problem/1904
