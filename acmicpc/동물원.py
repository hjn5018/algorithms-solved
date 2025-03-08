N = int(input())
if N == 1:
    print(3)
    quit()

dp = [0] * (N + 1)
dp[1] = 3
dp[2] = 7
for n in range(3, N + 1):
    dp[n] = (dp[n - 2] * 3 + (dp[n - 1] - dp[n - 2]) * 2)%9901

print(dp[N])

# https://www.acmicpc.net/problem/1309
# https://my-coding-notes.tistory.com/264
