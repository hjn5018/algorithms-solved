def solution(wallpaper):
    u, l, d, r = 0, 50, 0, 0
    for i in range(len(wallpaper)):
        if '#' in wallpaper[i]:
            u = i
            break
    for i in range(len(wallpaper)):
        if '#' in wallpaper[len(wallpaper) - 1 - i]:
            d = len(wallpaper) - i
            break
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if '#' == wallpaper[i][j] and j <= l:
                l = j
                break
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if '#' == wallpaper[i][len(wallpaper[i]) - 1 - j] and len(wallpaper[i]) - j >= r:
                r = len(wallpaper[i]) - j
                break
    return [u, l, d, r]
# https://school.programmers.co.kr/learn/courses/30/lessons/161990
