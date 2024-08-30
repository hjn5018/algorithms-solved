N = int(input())

if N == 1:
    print(0)
else:
    for i in range(1, int(N)):
        sum_ = i
        for digit in str(i):
            sum_ += int(digit)
        if sum_ == N:
            print(i)
            break
    if sum_ != N:
        print(0)
# https://www.acmicpc.net/problem/2231
