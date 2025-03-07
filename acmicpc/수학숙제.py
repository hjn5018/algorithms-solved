N = int(input())

def extract_nums(input_:str) -> list:
    list_ = []
    tmp = ''
    for i in range(len(input_)):
        if input_[i].isalpha():
            if tmp != '':
                list_.append(tmp)
                tmp = ''
        elif input_[i].isdigit():
            tmp += input_[i]
            if i == len(input_)-1:
                list_.append(tmp)
    return list_

def str_to_num(x:str) -> int:
    if x.count('0') == len(x):
        return 0
    if x[0] == '0':
        for i in range(1, len(x)):
            if x[i] != '0':
                return int(x[i:])
    return int(x)

all_nums = []
for _ in range(N):
    input_ = input()
    nums = extract_nums(input_)
    for num in nums:
        num = str_to_num(num)
        all_nums.append(num)

all_nums.sort()
for num in all_nums:
    print(num)

# https://www.acmicpc.net/problem/2870
