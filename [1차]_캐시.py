def solution(cacheSize, cities):
    answer = 0
    LRU = []
    for city in cities:
        if city.lower() in LRU:
            answer += 1
            LRU.remove(city.lower())
            LRU.append(city.lower())
        else:
            answer += 5
            if len(LRU) < cacheSize:
                LRU.append(city.lower())
            elif cacheSize != 0:
                LRU = LRU[1:] + [city.lower()]
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/17680
