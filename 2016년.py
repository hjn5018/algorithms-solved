def solution(a, b):
    answer = ''
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    # [1,2,3,4,5,6,7,8,9,10,11,12]
    # [0,3,1,3,2,3,2,3,3,2,3,2]
    # [0,3,4,0,2,5,0,3,6,1,4,6]
    # [0,3,-3,0,2,-2,0,3,-1,1,-3,-1]
    if a == 1:
        return day[b%7]
    if a == 2:
        return day[(b+31)%7]
    if a == 3:
        return day[(b+31+29)%7]
    if a == 4:
        return day[(b+31+29+31)%7]
    if a == 5:
        return day[(b+31+29+31+30)%7]
    if a == 6:
        return day[(b+31+29+31+30+31)%7]
    if a == 7:
        return day[(b+31+29+31+30+31+30)%7]
    if a == 8:
        return day[(b+31+29+31+30+31+30+31)%7]
    if a == 9:
        return day[(b+31+29+31+30+31+30+31+31)%7]
    if a == 10:
        return day[(b+31+29+31+30+31+30+31+31+30)%7]
    if a == 11:
        return day[(b+31+29+31+30+31+30+31+31+30+31)%7]
    if a == 12:
        return day[(b+31+29+31+30+31+30+31+31+30+31+30)%7]
      # https://school.programmers.co.kr/learn/courses/30/lessons/12901
