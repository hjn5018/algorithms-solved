def solution(code):
    answer = ''
    idx = 0
    mode = 0
    for i in code:
        if mode == 0:
            if code[idx] == '1':
                mode = 1
            else:
                if idx % 2 == 0:
                    answer += code[idx]
        else:
            if code[idx] == '1':
                mode = 0
            else:
                if idx % 2 == 1:
                    answer += code[idx]
        idx += 1
    return answer if answer != '' else 'EMPTY'
# https://school.programmers.co.kr/learn/courses/30/lessons/181932
