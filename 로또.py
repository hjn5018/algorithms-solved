from itertools import combinations
while True:
    input_ = input()
    if input_ == '0':
        break
    k, *S = map(int, input_.split())
    # print(k)
    # print(S)
    S.sort()

    for c in combinations(S, 6):
        print(*c)
    print()
# https://www.acmicpc.net/problem/6603
