N, B = input().split()
l = len(N)
B = int(B)
dict_ = {v: i for i, v in enumerate('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
answer = 0
for i, v in enumerate(N):
    answer += dict_[v] * (B ** (l - 1 - i))
print(answer)

# https://www.acmicpc.net/problem/2745
