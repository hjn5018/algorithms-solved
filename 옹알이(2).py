def solution(babbling):
    answer = 0
    for i in babbling:
        i = i.replace('aya', '1').replace('ye', '2').replace('woo', '3').replace('ma', '4')
        if i.isdigit():
            temp = ''
            count = 0
            for j in i:
                if temp == j:
                    break
                temp = j
                count += 1
                if count == len(i):
                    answer += 1
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/133499
