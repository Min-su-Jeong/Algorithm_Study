"""
1.전략
- 백트래킹(Backtracking)
- 방문 리스트(visited)를 생성하여 True -> 스타트팀 / False -> 링크팀 구분
- depth가 N의 절반에 도달했을 때 스타트팀과 링크팀의 차이 계산
- 재귀 호출

2.시간복잡도
- O(2^N) = 2^20 = 2,048 
  => 2초 이내 가능
"""
import sys; 
input = sys.stdin.readline

def backTracking(curNum, depth):
    global res
    
    # N의 절반인 경우 팀 능력치 차이 계산
    if depth == N//2:
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
    
    # 재귀 호출
    for i in range(curNum, N):
        if not visited[i]:
            visited[i] = True
            backTracking(i, depth+1)
            visited[i] = False
            
# 값 입력 및 초기화         
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
res = sys.maxsize

# 함수 실행
backTracking(0, 0)

# 결과 출력
print(res)