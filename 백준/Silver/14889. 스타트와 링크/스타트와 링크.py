"""
1.전략
- 백트래킹(Back Tracking)
- 스타트와 링크 팀을 나눌 때 스타트 팀 소속 제외한 나머지가 링크 팀
- BFS를 통해 오름차순 정렬(중복 방지) + N/2 만큼의 크기가 되었을 때 계산 시작
- S[i][j], S[j][i]와 대응되기 때문에 N*N/2 만큼 반복해서 계산 => N*N 만큼 반복 필요 X
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
def backTracking(curNum: int, depth: int):
    global res

    if depth == N//2:
        start, link = 0, 0

        for i in range(N):
            for j in range(i, N):
                if visited[i] and visited[j]:
                    start += (S[i][j] + S[j][i])

                elif not visited[i] and not visited[j]:
                    link += (S[i][j] + S[j][i])

        res = min(res, abs(start-link))
        return

    for i in range(curNum, N):
        if not visited[i]:
            visited[i] = True
            backTracking(i+1, depth+1)
            visited[i] = False

# Main          
backTracking(0, 0)

# Output  
print(res)