N = int(input())

if N == 1:
    pass
else:
# 2부터 N까지의 수 i로 N을 나눴을 때, 나머지가 0인 수를 찾는다.
    while True:
        for i in range(2, N+1):
            if N % i == 0:
                print(i)
                break
# 찾았다면 i로 N을 나눈 몫을 N으로 하고, 위 과정을 반복한다.
        N = N // i
# N이 1이 된다면 반복을 종료한다.
        if N == 1:
            break
# https://www.acmicpc.net/problem/11653
