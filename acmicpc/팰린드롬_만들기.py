from collections import Counter

def make_palindrome(name):
    # 문자의 빈도수 세기
    count = Counter(name)
    
    # 홀수로 나타나는 문자의 개수 세기
    odd_count = 0
    middle_char = ""
    half_palindrome = []
    
    for char, freq in count.items():
        if freq % 2 == 1:
            odd_count += 1
            middle_char = char  # 홀수 개수인 문자를 중간에 배치
            count[char] -= 1  # 홀수 개수인 문자는 하나 제외하고 짝수 개수만 남음
    
    # 홀수 개수인 문자가 2개 이상이면 팰린드롬을 만들 수 없다
    if odd_count > 1:
        return "I'm Sorry Hansoo"
    
    # 짝수 개수인 문자들을 반으로 나누어 앞부분을 만든다
    for char in sorted(count.keys()):  # 사전순으로 정렬
        half_palindrome.append(char * (count[char] // 2))
    
    # 반으로 나눈 부분을 이어 붙이고 중간 문자 (있다면)를 추가 후 다시 반대 방향으로 붙인다
    half_palindrome = ''.join(half_palindrome)
    return half_palindrome + middle_char + half_palindrome[::-1]

# 입력 받기
name = input().strip()

# 팰린드롬 만들기
result = make_palindrome(name)

# 결과 출력
print(result)

# https://www.acmicpc.net/problem/1213
