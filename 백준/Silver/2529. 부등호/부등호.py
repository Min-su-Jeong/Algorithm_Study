"""
1.전략
- 백트래킹(Back Tracking)
- 0 ~ 9 범위에서 중복 없는 수열 만들기
- 수열을 만들 때 부등호 조건에 만족할 경우에만 순회
- 조건에 충족하는 문자열 수열들을 res 변수에 저장
- res의 값에서 맨 마지막(최댓값)과 맨 첫번째(최솟값)를 출력

2.시간 복잡도
- 시간 제한: 1초
- O(10^N) = 10^8 = 100,000,000 
"""
import sys
input = sys.stdin.readline

# Input
k = int(input())
sign = list(input().split())

# Variables
res = []
visited = [False for _ in range(10)]

# Function 1. 부등호 관계 만족 여부 확인 함수
def check(a, b, op) -> bool:
    if op == '<':
        if a > b: 
            return False
    if op == '>':
        if a < b: 
            return False
        
    return True

# Function 2. 조건에 만족하는 최대/최소 값 구하는 함수
def backTracking(curNum: int, curStr: str):
    global res

    if curNum == k+1:
        res.append(curStr)
        return

    for i in range(10):
        if visited[i]:
            continue

        if curNum == 0 or check(curStr[curNum-1], str(i), sign[curNum-1]):
            visited[i] = True
            backTracking(curNum+1, curStr+str(i))
            visited[i] = False

# Main
backTracking(0, '')

# Output
print(res[-1])
print(res[0])