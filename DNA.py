N, M = map(int, input().split())
dnas = [input() for _ in range(N)]

ACGT = ('A', 'C', 'G', 'T')

s = ''
count = 0
for i in range(M):
    dict_ = {i:0 for i in ACGT}
    for j in range(N):
        dict_[dnas[j][i]] += 1
    list_ = list(dict_.items())
    list_.sort(key=lambda x: (-x[1], x[0]))
    s += list_[0][0]
    count += N - list_[0][1]
    
print(s)
print(count)

# https://www.acmicpc.net/problem/1969
