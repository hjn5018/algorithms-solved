def solution(lottos, win_nums):
    answer = []
    ranking = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    min, max = 0, 0
    for i in lottos:
        if i == 0:
            max += 1
        else:
            if i in win_nums:
                min += 1
                max += 1
    answer.append(ranking[max])
    answer.append(ranking[min])
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/77484
