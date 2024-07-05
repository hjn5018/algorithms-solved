def solution(s):
    answer = ''
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    nums = [i for i in range(10)]
    temp = ''
    for i in s:
        if i.isdigit():
            answer += i
        else:
            temp += i
            if temp in words:
                answer += str(dict(zip(words, nums))[temp])
                temp = ''
    return int(answer)
# https://school.programmers.co.kr/learn/courses/30/lessons/81301
