"""
1.전략
- DFS
- 인접 리스트 사용
- 친구 관계를 간선으로 표현하여 그래프 생성
- dfs 탐색 중 방문한 노드를 다시 방문할 수 있도록 백트래킹 구현

2.시간복잡도
- O(V+E) = 4,000 + 2,000 = 6,000 (Worst Case)
  => 2초 이내 가능
"""
import sys; 
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(f):
    global depth

    if depth == 5:
        print(1)
        sys.exit()

    visited[f] = True
    for i in graph[f]:
        if not visited[i]:
            depth += 1
            dfs(i)
            depth -= 1
            visited[i] = False

# 입력 받기
N, M = map(int,input().split())

# 필요한 변수 선언 및 초기화
depth = 1
visited = [False] * N
graph = [[] for _ in range(N)]

## 친구 관계 리스트 생성
for _ in range(M): 
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 함수 실행 및 결과 출력
for i in range(N):
    dfs(i)
    visited[i] = False

print(0)