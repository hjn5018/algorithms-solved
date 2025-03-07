N = int(input())
A = list(map(int, input().split()))

to_the_left, to_the_right, count = 0, 0, 0
for i in range(N):
    if A[i] % 2 == 0:
        to_the_left += i-count
        to_the_right += N-1-i-count
        count += 1

if to_the_left > to_the_right:
    print(to_the_right)
else:
    print(to_the_left)
# https://www.acmicpc.net/problem/25379
