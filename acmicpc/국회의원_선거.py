N = int(input())
votes = [int(input()) for i in range(N)]

dasom = votes[0]
votes_without_dasom = votes[1:]

if len(votes) == 1:
    print(0)
elif dasom > max(votes_without_dasom):
    print(0)
elif dasom <= max(votes_without_dasom):
    count = 0
    while True:
        idx = votes_without_dasom.index(max(votes_without_dasom))
        votes_without_dasom[idx] -= 1
        dasom += 1
        count += 1
        if dasom > max(votes_without_dasom):
            break
    print(count)
# https://www.acmicpc.net/problem/1417
