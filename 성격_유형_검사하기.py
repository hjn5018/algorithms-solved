def solution(survey, choices):
    answer = ''
    weights = {'A':0, 'N':0, 'C':0, 'F':0, 'M':0, 'J':0, 'R':0, 'T':0}
    for i in range(len(survey)):
        if choices[i] < 4:
            weights[survey[i][0]] += abs(choices[i] - 4)
        else:
            weights[survey[i][1]] += abs(choices[i] - 4)
    if weights['R'] >= weights['T']:
        answer += 'R'
    else:
        answer += 'T'
    if weights['C'] >= weights['F']:
        answer += 'C'
    else:
        answer += 'F'
    if weights['J'] >= weights['M']:
        answer += 'J'
    else:
        answer += 'M'
    if weights['A'] >= weights['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/118666
