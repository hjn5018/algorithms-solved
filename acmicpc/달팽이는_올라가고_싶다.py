A, B, V = map(int, input().split())

answer = 0

if (V - A) % (A - B) == 0:
    answer += (V - A) // (A - B)
else:
    answer += (V - A) // (A - B) + 1

answer += 1

print(answer)
# https://www.acmicpc.net/problem/2869
