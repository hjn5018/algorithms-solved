N = int(input())

participants = {}
for _ in range(N):
    participant = input()
    if participant in participants:
        participants[participant] += 1
    else:
        participants[participant] = 1

for _ in range(N-1):
    finish = input()
    participants[finish] -= 1

for i, v in participants.items():
    if v != 0:
        print(i)
# https://www.acmicpc.net/problem/10546
