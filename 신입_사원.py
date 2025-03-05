import sys

def select_recruits(applicants):
    # 서류 성적 기준으로 정렬
    applicants.sort(key=lambda x: x[0])
    
    # 첫 번째 지원자의 면접 성적을 초기 기준으로 설정
    count = 1
    min_interview_rank = applicants[0][1]
    
    # 정렬된 배열을 순회하며 채용 가능한 지원자 수 계산
    for i in range(1, len(applicants)):
        # 현재 지원자의 면접 성적이 기존 최소 면접 순위보다 좋으면
        if applicants[i][1] < min_interview_rank:
            count += 1
            min_interview_rank = applicants[i][1]
    
    return count

# 입력 처리
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    applicants = []
    
    for _ in range(N):
        document_rank, interview_rank = map(int, sys.stdin.readline().split())
        applicants.append((document_rank, interview_rank))
    
    # 최대 채용 가능 인원 출력
    print(select_recruits(applicants))
# https://www.acmicpc.net/submit/1946/90894077
