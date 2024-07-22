def solution(players, callings):
    rank = {}
    for i in range(len(players)):
        rank[players[i]] = i
    for i in callings:
        players[rank[i]], players[rank[i] - 1] = players[rank[i] - 1], players[rank[i]]
        print(f'{rank[i] = }')
        print(f'{rank[players[rank[i]]]} = ')
        rank[i] = rank[i] - 1
        rank[players[rank[i]]] = rank[players[rank[i]]] + 1
        print(f'{rank[i] = }')
        print(f'{rank[players[rank[i]]]} = ')
        break
    return players
# https://school.programmers.co.kr/learn/courses/30/lessons/178871
