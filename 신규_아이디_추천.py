def solution(new_id):
    new_id = new_id.lower() # 1
    new_id = ''.join([i for i in new_id if i in 'abcdefghijklmnopqrstuvwxyz-_.0123456789']) # 2
    while '..' in new_id:
        new_id = new_id.replace('..', '.') # 3
    if new_id:
        if new_id[0] == '.':
            new_id = new_id[1:]
    if new_id:
        if new_id[-1] == '.':
            new_id = new_id[:-1] # 4
    if not new_id:
        new_id += 'a' # 5
    if len(new_id) >= 16:
        new_id = new_id[:15] # 6
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    while len(new_id) <= 2:
        new_id += new_id[-1] # 7
    return new_id
# https://school.programmers.co.kr/learn/courses/30/lessons/72410
