def solution(numbers):
    sum_list = []
    for i in range(len(numbers)):
        for j in numbers[i+1:]:
            if numbers[i]+j in sum_list:
                pass
            else:
                sum_list.append(numbers[i]+j)
    return sorted(sum_list)
# https://school.programmers.co.kr/learn/courses/30/lessons/68644
