def solution(sizes):
    for i, (w, h) in enumerate(sizes):
        if w < h:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    max_w, max_h = 0, 0
    for w, h in sizes:
        if w > max_w:
            max_w = w
        if h > max_h:
            max_h = h
    return max_w * max_h
# https://school.programmers.co.kr/learn/courses/30/lessons/86491
