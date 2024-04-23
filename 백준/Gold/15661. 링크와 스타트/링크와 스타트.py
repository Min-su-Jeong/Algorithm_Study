"""
1.전략
- 백트래킹(Backtracking)
- 방문 리스트(visited)를 생성하여 True -> 스타트팀 / False -> 링크팀 구분
- 조합에 따라 스타트팀과 링크팀으로 나눠 차이를 구하고, 최솟값 갱신
- 재귀 호출

2.시간복잡도
- O(2^N) = 2^20 = 1,048,576
  => 2초 이내 가능
"""
import sys
input = sys.stdin.readline

def backTracking():
    global res
    start, link = 0, 0

    # NxN을 돌면서 방문여부에 따라 팀 구분
    for i in range(N):
        for j in range(N):
            # 스타트팀 능력치 계산
            if visited[i] and visited[j]:
                start += graph[i][j]

            # 링크팀 능력치 계산
            elif not visited[i] and not visited[j]:
                link += graph[i][j]

    # 능력치 차가 최소가 되는 값 찾기            
    res = min(res, abs(start-link))
    return
    
def solution(iters):
    if iters == N:
        backTracking()
        return
    
    visited[iters] = True
    solution(iters+1)
    visited[iters] = False
    solution(iters+1)
    

# 값 입력 및 초기화         
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
res = sys.maxsize

# 함수 실행
solution(0)

# 결과 출력
print(res)