res, n = 0, 0
visited = []

def dfs(k, cnt, dungeons):
    global res
    if cnt > res: # 현재 결과보다 최대 방문 가능 횟수가 큰 경우
        res = cnt # 최대 방문 횟수 초기화
    
    if cnt == n:   # 던전의 개수만큼 모두 방문 가능하면  
        return cnt # 즉시 cnt 값 반환하여 탐색 시간 줄이기
    
    for i in range(n):
    	# 피로도가 충분하지만 아직 방문하지 않은 경우
        if k >= dungeons[i][0] and not visited[i]:
        	# 방문 처리
            visited[i] = 1
            # 줄어든 피로도로 던전 방문 시작
            dfs(k - dungeons[i][1], cnt+1, dungeons)
            # 해당 순서로 던전을 모두 방문하여 재초기화
            visited[i] = 0

def solution(k, dungeons):
    global n, visited
    n = len(dungeons)
    visited = [0] * n
    dfs(k, 0, dungeons)
    
    return res
