def solution(s, skip, index):
    answer = ''
    alphabet = set(chr(i) for i in range(97, 123))
    remainder = alphabet - set(skip)
    letters = sorted(remainder)
    for i in s:
        if letters.index(i) + index <= len(letters) - 1:
            answer += letters[letters.index(i) + index]
        else:
            answer += letters[(letters.index(i) + index) % len(letters)]
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/155652
