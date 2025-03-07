def solution(nums):
    answer = 0
    if len(nums)/2 <= len(set(nums)):
        return len(nums)/2
    return len(set(nums))
  # https://school.programmers.co.kr/learn/courses/30/lessons/1845
