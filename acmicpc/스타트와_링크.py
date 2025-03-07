from itertools import combinations

def calc_team_score(team, S):
    score = 0
    for i in team:
        for j in team:
            score += S[i][j]
    return score

def solve(N, S):
    people = list(range(N))
    min_diff = float('inf')

    for start_team in combinations(people, N // 2):
        link_team = list(set(people) - set(start_team))

        start_score = calc_team_score(start_team, S)
        link_score = calc_team_score(link_team, S)

        min_diff = min(min_diff, abs(start_score - link_score))

    return min_diff

# 입력 받기
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

# 최소 능력치 차이 출력
print(solve(N, S))

# https://www.acmicpc.net/problem/14889
