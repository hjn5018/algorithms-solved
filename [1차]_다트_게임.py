def solution(dartResult):
    answer = 0
    index = 0
    end_index = 0
    past_cal = 0
    for _ in range(3):
        cal = 0
        while dartResult[index].isdigit():
            index += 1
        if dartResult[index] == 'S':
            cal += int(dartResult[end_index:index])
        elif dartResult[index] == 'D':
            cal += int(dartResult[end_index:index]) ** 2
        elif dartResult[index] == 'T':
            cal += int(dartResult[end_index:index]) ** 3
        index += 1
        if len(dartResult) < index + 1:
            answer += cal
            break
        if dartResult[index] == '*':
            answer -= past_cal
            cal *= 2
            past_cal *= 2
            answer += cal + past_cal
            end_index = index + 1
            index += 1
            past_cal = cal
            continue
        elif dartResult[index] == '#':
            cal *= -1
            end_index = index + 1
            index += 1
            answer += cal
            past_cal = cal
            continue
        answer += cal
        past_cal = cal
        end_index = index
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/17682
