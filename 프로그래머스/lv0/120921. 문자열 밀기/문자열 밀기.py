from collections import deque # deque 자료구조 사용

def solution(A, B):
    A, B = deque(A), deque(B) # A, B를 모두 deque로 사용
    for i in range(len(A)):   # A의 길이만큼 반복
        if A == B:            # 만약 A와 B가 같으면
            return i          # 밀어야 하는 최소 횟수 반환
        A.rotate()            # A와 B가 다르면 rotate() 함수를 이용하여 문자열 밀기
    return -1                 # 밀어서 B가 될 수 없으면 -1 반환