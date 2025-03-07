N, K = map(int, input().split())

list_ = [ _ for _ in range(2, N+1)]
remove = 0
while True:
    l = len(list_)
    pointer = 0
    count = 0
    m = list_[0]
    while pointer + count <= l - 1:
        if list_[pointer] % m == 0:
            count += 1
            remove += 1
            if remove == K:
                print(list_.pop(pointer))
                break
            else:
                list_.remove(list_[pointer])
        else:
            pointer += 1
    if remove >= K:
        break
# https://www.acmicpc.net/problem/2960
