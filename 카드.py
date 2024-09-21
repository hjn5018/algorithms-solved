N = int(input())

dict_ = {}
for i in range(N):
    key = input()
    if key in dict_:
        dict_[key] += 1
    else:
        dict_[key] = 1

values = list(dict_.values())
keys = list(dict_.keys())
# print(f"{values = }")
# print(f"{keys = }")
list_ = []
for i in range(len(values)):
    tmp = []
    tmp.append(values[i])
    tmp.append(int(keys[i]))
    list_.append(tmp)

# print(f"{list_ = }")
list_.sort(key=lambda x: x[1])
# print(f"{list_ = }")
list_.sort(reverse=True, key=lambda x: x[0])
# print(f"{list_ = }")
print(list_[0][1])
# https://www.acmicpc.net/problem/11652
