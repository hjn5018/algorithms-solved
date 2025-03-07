def solution(numer1, denom1, numer2, denom2):
    answer = [0,0]
    answer[0] = numer1*denom2 + numer2*denom1
    answer[1] = denom1*denom2
    for i in range(min(answer[0], answer[1]), 0, -1):
        if answer[0] % i == 0 and answer[1] % i == 0:
            answer[0] = answer[0] // i
            answer[1] = answer[1] // i
    return answer
  # https://school.programmers.co.kr/learn/courses/30/lessons/120808
