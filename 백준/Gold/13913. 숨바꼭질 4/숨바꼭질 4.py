"""
1. 전략
- BFS (Breadth-First Search)
- 조건(x-1, x+1, x*2) 인덱스에 이전 경로 저장

2. 시간복잡도
- O(N) = 100,001
  => 
"""
from collections import deque

def BFS(N: int, K: int):
    global move

    res = []
    q = deque([N])
    while q:
        cur = q.popleft()

        if cur == K:
            while cur != N:     	
                res.append(cur)	
                cur = move[cur]	
            res.append(N)
            break

        for m in (cur-1, cur+1, cur << 1):
            if 0 <= m < MAX and move[m] == -1:
                move[m] = cur
                q.append(m)

    return res

# 입력 받기
N, K = map(int, input().split())

# 필요한 변수 생성 및 초기화
MAX = 100001
move = [-1] * MAX
move[N] = N

# 함수 실행
res = BFS(N, K)

# 결과 출력
print(len(res)-1)
print(*res[::-1])