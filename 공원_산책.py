def solution(park, routes):
    answer = []
    H = len(park)
    W = len(park[0])
    for i in range(len(park)):
        if 'S' in park[i]:
            for j in range(len(park[i])):
                if park[i][j] == 'S':
                    answer = [i, j]
                    break
            break

    h, w = answer
    h, w = int(h), int(w)
    flag = True
    for i in routes:
        if i[0] == 'E':
            if w + int(i[2]) < W:
                for j in range(w, w + int(i[2]) + 1):
                    print(f'{j = }')
                    print(f'{park[h][j] = }')
                    if park[h][j] == 'X':
                        flag = False
                        break
                if flag:
                    w += int(i[2])
                else:
                    flag = True
        if i[0] == 'W':
            if w - int(i[2]) >= 0:
                for j in range(w - int(i[2]), w + 1):
                    if park[h][j] == 'X':
                        flag = False
                        break
                if flag:
                    w -= int(i[2])
                else:
                    flag = True
        if i[0] == 'N':
            if h - int(i[2]) >= 0:
                for j in range(h - int(i[2]), h + 1):
                    if park[j][w] == 'X':
                        flag = False
                        break
                if flag:
                    h -= int(i[2])
                else:
                    flag = True
        if i[0] == 'S':
            if h + int(i[2]) < H:
                for j in range(h, h + int(i[2]) + 1):
                    if park[j][w] == 'X':
                        flag = False
                        break
                if flag:
                    h += int(i[2])
                else:
                    flag = True
    return [h, w]
# https://school.programmers.co.kr/learn/courses/30/lessons/172928
