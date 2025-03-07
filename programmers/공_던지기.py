def solution(numbers, k):
    ball_pass_list = []
    for j in range(len(numbers)):
        if (1 + 2*j) > len(numbers):
            ball_pass_list.append((1 + 2*j)%len(numbers))
        else:
            ball_pass_list.append(1 + 2*j)
    
    i = 0
    if len(numbers) % 2:
        i = k % len(numbers)
    else:
        i = k % (len(numbers) // 2)
    return ball_pass_list[i-1]
# https://school.programmers.co.kr/learn/courses/30/lessons/120843
