from collections import deque # 양방향 큐 모듈 사용

def solution(cards1, cards2, goal):
    q1 = deque(list(cards1)) # cards1을 양방향 큐 자료형으로 변환
    q2 = deque(list(cards2)) # cards2를 양방향 큐 자료형으로 변환
    
    for g in goal:              # goal 내의 요소 순차적으로 꺼내기
        if q1 and q1[0] == g:   # 각 카드의 맨 앞 단어들 비교 후, 
            q1.popleft()        # 같은 단어가 있으면 첫 번째에 위치한 단어 pop
        elif q2 and q2[0] == g:
            q2.popleft()
        else:                   # 두 가지 경우에 속하지 않는 경우,
            return "No"         # "No" 출력
        
    return "Yes"