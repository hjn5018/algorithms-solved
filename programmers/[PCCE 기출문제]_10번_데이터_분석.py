def solution(data, ext, val_ext, sort_by):
    answer = []
    for i in data:
        for j in range(len(i)):
            if ext == 'code':
                if j == 0 and i[j] < val_ext:
                    answer += [i]
            if ext == 'date':
                if j == 1 and i[j] < val_ext:
                    answer += [i]
            if ext == 'maximum':
                if j == 2 and i[j] < val_ext:
                    answer += [i]
            if ext == 'remain':
                if j == 3 and i[j] < val_ext:
                    answer += [i]
    if sort_by == 'code':
        answer.sort(key=lambda x:x[0])
    if sort_by == 'date':
        answer.sort(key=lambda x:x[1])
    if sort_by == 'maximum':
        answer.sort(key=lambda x:x[2])
    if sort_by == 'remain':
        answer.sort(key=lambda x:x[3])
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/250121
