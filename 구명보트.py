from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    people = deque(people)
    while True:
        if len(people) > 1 and people[0] + people[-1] <= limit:
            answer += 1
            people.popleft()
            people.pop()
        else:
            people.popleft()
            answer += 1
        if not people:
            return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/42885
