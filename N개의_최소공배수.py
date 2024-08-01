def cal_lcm(arr):
    a = arr.pop()
    b = arr.pop()
    gcd = 1
    for i in range(min(int(a), b), 1, -1):
        if a % i == 0 and b % i == 0:
            gcd *= i
            a /= i
            b /= i
    lcm = a * b * gcd
    arr.append(lcm)
    
def solution(arr):
    while len(arr) > 1:
        cal_lcm(arr)
    return int(arr[0])
# https://school.programmers.co.kr/learn/courses/30/lessons/12953
