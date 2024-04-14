"""
1.전략
- 백트래킹
- 리스트 arr의 중복 여부 확인
- 중복이 아닌 경우, 숫자 i 넣기
- 재귀함수에서 M개를 선택할 경우 출력

2.시간복잡도
중복 가능인 경우 : O(N^2) = 8 * 8 = 64
중복 불가능인 경우 : O(N!) = 10! = 3,628,800
=> 1초 내 가능
"""

def backTracking():
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        if i not in arr:
            arr.append(i)
            backTracking()
            arr.pop()
        

N, M = map(int, input().split())
arr = []

backTracking()