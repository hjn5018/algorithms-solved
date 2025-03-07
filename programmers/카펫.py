def solution(brown, yellow):
    answer = []
    x = ((4 + brown)**2 - 16 * (brown + yellow))**1/2
    w = (4 + brown + ((4 + brown)**2 - 16 * (brown + yellow))**(1/2)) / 4
    h = ((brown + 4) / 2) - w
    return [w, h]
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    # (w + h) * 2 = brown + 4
    # (w - 2) * (h - 2) = yellow
    # brown + yellow = w * h    
    candidate = []
    for i in range(1, int((brown + yellow)**(1/2)) + 1):
        if (brown + yellow) % i == 0:
            candidate.append((i, (brown + yellow)//i))
            
    for h, w in candidate:
        if (w + h) * 2 == brown + 4:
            if (w - 2) * (h - 2) == yellow:
                return [w, h]
        
