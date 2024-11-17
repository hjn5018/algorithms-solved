import math

# 입력 받기
n, m = map(int, input().split())

# nCm 계산
result = math.factorial(n) // (math.factorial(m) * math.factorial(n - m))

# 결과 출력
print(result)

# https://www.acmicpc.net/problem/2407
