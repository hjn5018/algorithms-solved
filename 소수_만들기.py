def solution(nums):
    answer = 0
    sumlist = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                sumlist.append(nums[i] + nums[j] + nums[k])
    
    for i in sumlist:
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count == 2:
            answer += 1
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/12977
