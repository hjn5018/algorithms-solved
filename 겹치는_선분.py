def solution(lines):
    arr1 = [i for i in range(lines[0][0], lines[0][1])]
    arr2 = [i for i in range(lines[1][0], lines[1][1])]
    arr3 = [i for i in range(lines[2][0], lines[2][1])]
    set4 = set(arr1 + arr2 + arr3)
    arr5 = [0]*len(set4)
    
    for i,v in enumerate(set4):
        if v in arr1:
            arr5[i] += 1
        if v in arr2:
            arr5[i] += 1
        if v in arr3:
            arr5[i] += 1
    return len([i for i in arr5 if i >= 2])
  # https://school.programmers.co.kr/learn/courses/30/lessons/120876
