T = int(input())

for _ in range(T):
    N = int(input())
    note1 = set(map(int, input().split()))
    M = int(input())
    note2 = list(map(int, input().split()))
    for i in note2:
        if i in note1:
            print(1)
        else:
            print(0)
# https://www.acmicpc.net/problem/2776
