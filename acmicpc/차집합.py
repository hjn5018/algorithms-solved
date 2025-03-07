n, m = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

list_ = []
for element in A:
    if element not in B:
        list_.append(element)

if not list_:
    print(0)
else:
    print(len(list_))
    print(*sorted(list_))
# https://www.acmicpc.net/problem/1822
