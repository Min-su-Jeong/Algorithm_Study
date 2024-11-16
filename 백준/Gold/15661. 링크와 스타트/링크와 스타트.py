"""
1.전략
- 백트래킹(Back Tracking)
- 스타트와 링크 팀을 나눌 때 스타트 팀 소속 제외한 나머지가 링크 팀
- DFS와 최솟 값 계산 함수 분리 => 팀의 인원을 맞추지 않아도 되는 조건 때문
- Visited가 True인 이후와 False인 이후 각각에 대해 재귀 호출
- 결과 값(res)과 스타트 링크 팀의 점수 차이를 비교해서 최소를 갖는 해를 업데이트

2.시간 복잡도
- 제한 시간: 2초
- O(2^N) = 2 ^ 20 = 1,048,576
"""
import sys
input = sys.stdin.readline

# Input
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

# Variables
res = sys.maxsize
visited = [False for _ in range(N)]

# Solution
def calc():
    global res

    start, link = 0, 0

    for i in range(N):
        for j in range(i, N):
            if visited[i] and visited[j]:
                start += (S[i][j] + S[j][i])

            elif not visited[i] and not visited[j]:
                link += (S[i][j] + S[j][i])

    res = min(res, abs(start-link))
    return


def backTracking(curNum: int):
    if curNum == N:
        calc()
        return
    
    visited[curNum] = True
    backTracking(curNum+1)
    visited[curNum] = False
    backTracking(curNum+1)

# Main          
backTracking(0)

# Output  
print(res)