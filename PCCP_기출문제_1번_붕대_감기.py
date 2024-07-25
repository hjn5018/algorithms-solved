def solution(bandage, health, attacks):
    answer = health
    idx = 0
    consecutive = 0
    t, x, y = bandage
    attack_time = [attack_time for attack_time, damage in attacks]
    damage = [damage for attack_time, damage in attacks]
    while idx <= max(attack_time):
        if idx in attack_time:
            answer -= damage[attack_time.index(idx)]
            consecutive = 0
            if answer <= 0:
                return -1
        else:
            if idx != 0:
                consecutive += 1
                answer = min(answer + x, health)
            if consecutive == t:
                answer = min(answer + y, health)
                consecutive = 0
        idx += 1
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/250137
