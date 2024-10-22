N = int(input())

list_ = [list(map(int, input().split())) for i in range(N)]

list_.sort(key=lambda x: x[0])
t = list_[0][0] + list_[0][1]

for i in range(1, len(list_)):
    if t < list_[i][0]:
        t = list_[i][0] + list_[i][1]
    elif t >= list_[i][0]:
        t += list_[i][1]

print(t)
# https://solved.ac/problems/level/7?sort=solved&direction=desc&page=2
