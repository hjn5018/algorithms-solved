N = int(input())
n = 1
while True:
    N -= n
    if N <= 0:
        break
    n += 1
N += n
if n % 2 == 0:
    list_ = [f"{i}/{n-i+1}" for i in range(1, n+1)]
else:
    list_ = [f"{n-i+1}/{i}" for i in range(1, n+1)]
answer = list_[N-1]
print(answer)
# https://www.acmicpc.net/problem/1193
