N, M = map(int, input().split())

dict_ = {}
for _ in range(N):
    data = input().split()
    dict_[data[0]] = data[1]

for i in range(M):
    print(dict_[input()])
# https://www.acmicpc.net/problem/17219
