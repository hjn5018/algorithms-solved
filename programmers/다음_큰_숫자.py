def solution(n):
    answer = 0
    bin_ = bin(n)[2:]
    idx = 0
    erased = 0
    for i in range(len(bin_)-1, 0, -1):
        if bin_[i] == '1':
            idx = i
            break
            
    while bin_[idx - 1] == '1':
        erased += 1
        idx -= 1
        if idx - 1 < 0:
            break
    idx += erased
    
    n += (2**(len(bin_) - 1 - idx))
    for i in range(erased):
        n += (2**i)
    return n
# https://school.programmers.co.kr/learn/courses/30/lessons/12911
