def solution(babbling):
    answer = 0
    after = []
    for i in babbling:
        if 'aya' in i:
            idx = i.index('aya')
            i = i[:idx] + ' ' + i[idx+len('aya'):]
        if 'ye' in i:
            idx = i.index('ye')
            i = i[:idx] + ' ' + i[idx+len('ye'):]
        if 'woo' in i:
            idx = i.index('woo')
            i = i[:idx] + ' ' + i[idx+len('woo'):]
        if 'ma' in i:
            idx = i.index('ma')
            i = i[:idx] + ' ' + i[idx+len('ma'):]
        after.append(i)
    print(after)
    for i in after:
        if i.split() == []:
            answer += 1
    return answer
  # https://school.programmers.co.kr/learn/courses/30/lessons/120956
