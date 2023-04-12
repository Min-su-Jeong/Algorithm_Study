from collections import deque # 양방향 큐(deque) 모듈 사용

def solution(n, m , section):
    res = 0					 # 페인트를 칠해야하는 최소 횟수
    section = deque(section) # section 양방향 큐 자료형으로 변환
    
    while section:                                # 페인트칠이 끝날때까지 반복
        start = section.popleft()                 # 페인트칠 시작 지점
        while section and start + m > section[0]: # 페인트칠 시작 지점부터 롤러의 길이(m)만큼 칠하기
            section.popleft() 
        res += 1
    
    return res