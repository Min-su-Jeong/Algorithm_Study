"""
1.전략
- 백트래킹(Back Tracking)
- [오름차순 + 중복 X]인 수열 만들기 문제와 유사
- 0이 나오기 전까지 테스트 케이스 연속 출력

2.시간 복잡도
- 시간 제한: 1초
- O(N^6) = 12^6 = 2,985,984
"""
import sys
input = sys.stdin.readline

# Solution
def backTracking(curNum: int):
    global arr

    if len(arr) == 6:
        print(*arr)
        return
    
    for i in range(curNum, K):
        arr.append(S[i])
        backTracking(i+1)
        arr.pop()

while True:
    # Input
    T = list(map(int, input().split()))
    K, S = T[0], T[1:]
    
    # Variables
    arr = []

    # Main
    if K == 0:
        break
    else:
        backTracking(0)
        print()