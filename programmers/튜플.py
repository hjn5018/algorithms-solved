def solution(s):
    answer = []
    s = s[1:-1]
    flag = False
    list_ = []
    for i in s:
        if i == '{':
            flag = True
            list_1 = []
            str_ = ''
            continue
        if i == '}':
            flag = False
            list_1.append(str_)
            list_.append(list_1)
            continue
        if flag and i != ',':
            str_ += i
        if i == ',' and flag:
            list_1.append(str_)
            str_ = ''
    list_.sort(key=lambda x: len(x))
    for i in list_:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/64065
