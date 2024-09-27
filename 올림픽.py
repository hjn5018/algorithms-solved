N, K = map(int, input().split())

list_ = []
for _ in range(N):
    country, gold, silver, bronze = map(int, input().split())
    list_.append([country, [gold, silver, bronze]])
list_.sort(reverse=True, key=lambda x: x[1])

for i in range(N):
    if i == 0:
        list_[i].append(1)
    else:
        if list_[i][1] == list_[i-1][1]:
            list_[i].append(list_[i-1][2])
        else:
            list_[i].append(i+1)

for i in list_:
    if i[0] == K:
        print(i[2])
# https://www.acmicpc.net/problem/8979
