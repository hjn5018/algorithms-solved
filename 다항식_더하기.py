def solution(polynomial):
    answer = ''
    x_list = [1 if i.strip() == 'x' else int(i.strip().strip('x')) for i in polynomial.split('+') if 'x' in i]
    constant_list = [int(i) for i in polynomial.split('+') if 'x' not in i]
    if sum(x_list) != 0:
        if sum(x_list) == 1:
            answer += 'x'
        else:
            answer += str(sum(x_list)) + 'x'
        if sum(constant_list) != 0:
            answer += ' + '+ str(sum(constant_list))
    elif sum(x_list) == 0:
        if sum(constant_list) != 0:
            answer += str(sum(constant_list))
        else:
            pass
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/120863
