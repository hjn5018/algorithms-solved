def solution(id_list, report, k):
    report = list(set(report))
    report = [i.split() for i in report]
    reported_dict = {id : 0 for id in id_list}
    reporter_dict = {id : 0 for id in id_list}
    for i in report:
        reported_dict[i[1]] += 1
    for i, v in reported_dict.items():
        if v >= k:
            for j, l in report:
                if i == l:
                    reporter_dict[j] += 1
    return list(reporter_dict.values())
# https://school.programmers.co.kr/learn/courses/30/lessons/92334?language=python3
