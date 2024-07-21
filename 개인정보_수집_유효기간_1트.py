def solution(today, terms, privacies):
    answer = []
    y, m, d = 0, 0, 0
    due_y, due_m, due_d = 0, 0, 0
    for i in privacies:
        for j in range(len(terms)):
            if i[-1] == terms[j][0]:
                y, m, d = i.split(' ')[0].split('.')
                print(f'{y + m + d = }')
                print(f'{terms[j] = }')
                due_y = int(y) + ((int(m) + int(terms[j].split(' ')[1])) // 13)
                due_m = 1 if (int(m) + int(terms[j].split(' ')[1])) % 13 == 0 else (int(m) + int(terms[j].split(' ')[1])) % 13
                due_d = d
                due_y = str(due_y)
                due_m = '0' + str(due_m) if due_m < 10 else str(due_m)
                due_d = str(due_d)
                print(f'{due_y + due_m + due_d = }')
                print(f'{int(due_y + due_m + due_d) = }')
                print(f"{today.replace('.', '') = }")
                if int(due_y + due_m + due_d) <= int(today.replace('.', '')):
                    answer += [privacies.index(i) + 1]
    return answer
  # https://school.programmers.co.kr/learn/courses/30/lessons/150370
