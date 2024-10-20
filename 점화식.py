n = int(input())

list_ = [0] * (n+1)
list_[0] = 1

if n == 0:
    print(1)
else:
    for j in range(1, n+1):
        for i in range(j):
            list_[j] += list_[i] * list_[j-1-i]

    print(list_[n])
# https://www.acmicpc.net/problem/13699
