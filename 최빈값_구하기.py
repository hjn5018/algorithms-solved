def solution(array):
    element = []
    count = []
    for i in array:
        if i not in element:
            element.append(i)
            count.append(array.count(i))
            
    if count.count(max(count)) > 1:
        return -1
    else:
        return element[count.index(max(count))]
# https://school.programmers.co.kr/learn/courses/30/lessons/120812
