M, N = map(int, input().split())
num_to_string = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}

nums = [i for i in range(M, N+1)]
nums_in_string = []
for i in range(M, N+1):
    str_ = ''
    for j in range(len(str(i))):
        str_ += num_to_string[int(str(i)[j])]
        if j != len(str(i))-1:
            str_ += ' '
    nums_in_string.append((i, str_))
nums_in_string = (nums_in_string)
nums_in_string.sort(key=lambda x: x[1])

idx = 0
while idx < len(nums):
    print(nums_in_string[idx][0], end=' ')
    idx += 1
    if idx % 10 == 0:
        print()
# https://www.acmicpc.net/problem/1755
