def solution(friends, gifts):
    record = {j : {i : 0 for i in friends} for j in friends}
    # record = {'a': {'a': 0, 'b': 0, 'c': 0}, 'b': {'a': 0, 'b': 0, 'c': 0}, 'c': {'a': 0, 'b': 0, 'c': 0}}
    
    gifts = [gift.split() for gift in gifts]
    # gifts = [['a', 'b'], ['b', 'a'], ['c', 'a'], ['a', 'c'], ['a', 'c'], ['c', 'a']]
    
    for gift in gifts:
        record[gift[0]][gift[1]] += 1

    index = {i : [0, 0] for i in friends}
    # index = {'a': [0, 0], 'b': [0, 0], 'c': [0, 0]}
    
    for i, j in gifts:
        index[i][0] += 1
        index[j][1] += 1
    
    present_indices = {i : index[i][0] - index[i][1] for i in index}
    
    predict = {i : 0 for i in friends}
    # predict = {'a': 0, 'b': 0, 'c': 0}
    
    count = 0
    for i in friends:
        for j in friends[friends.index(i)+1:]:
            count += 1
            if record[i][j] == record[j][i]:
                # 선물지수 비교
                if present_indices[i] == present_indices[j]:
                    pass
                elif present_indices[i] > present_indices[j]:
                    predict[i] += 1
                elif present_indices[i] < present_indices[j]:
                    predict[j] += 1
            elif record[i][j] > record[j][i]:
                predict[i] += 1
            elif record[i][j] < record[j][i]:
                predict[j] += 1
    return max(predict.values())
# https://school.programmers.co.kr/learn/courses/30/lessons/258712
