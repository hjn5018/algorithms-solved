N, K = map(int, input().split())

min_ = sum(range(1, K+1))
if N >= min_:
    if (N-min_) % K == 0:
        print(K-1)
    else:
        print(K)
else:
    print(-1)
# https://www.acmicpc.net/problem/19939
