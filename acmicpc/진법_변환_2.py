N, B = input().split()
dict_ = {i: v for i, v in enumerate('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
temp = ''
while True:
    a, b = divmod(int(N), int(B))
    temp += dict_[b]
    if a == 0:
        break
    N = a

answer = ''
for i in reversed(temp):
    answer += i
print(answer)
# https://www.acmicpc.net/problem/11005
