"""
1.전략
- 브루트포스
- N의 범위가 작으므로 모든 순열을 구해서 차이가 최대인 조합을 찾음.

2.시간복잡도
- O(N!) = 8! = 40,320(Worst case)
  => 1초 이내 가능
"""
def dfs(curList: list):
    global res
    
    if len(curList) == N:
        # 수식 대입
        maxDiff = sum(abs(curList[i-1] - curList[i]) for i in range(1, N))
        
        # 최댓값 갱신
        res = max(res, maxDiff)
        return
    
    # 모든 순열 순회
    for i in range(N):
        # 방문 여부에 따른 순회
        if not visited[i]:
            visited[i] = True
            curList.append(arr[i])
            dfs(curList)
            visited[i] = False
            curList.pop()
            
# 파라미터        
N = int(input())
arr = list(map(int, input().split()))
visited = [False] * N
res = 0

# 함수 실행
dfs([])

# 결과 출력
print(res)