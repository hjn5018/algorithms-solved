def solution(numlist, n):
    distance_list = []
    for num in numlist:
        distance_list.append((abs(num-n), num))
        
    a = sorted(distance_list)
    while True:
        flag = False
        for i in range(len(numlist)-1):
            if a[i][0] == a[i+1][0]:
                if a[i][1] < a[i+1][1]:
                    a[i], a[i+1] = a[i+1], a[i]
                    flag = True
        if flag == False:
            break
    
    answer = [a[i][1] for i in range(len(a))]
    return answer
  # https://school.programmers.co.kr/learn/courses/30/lessons/120880#
