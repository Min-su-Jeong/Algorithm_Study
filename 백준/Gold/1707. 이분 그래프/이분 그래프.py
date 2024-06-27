"""
1. 전략
- DFS
- 인접 리스트 사용
- 인접 노드로 탐색 -> 현재 집합과 다른 집합 표시 
   -> 인접 노드 중 현재 노드의 집합과 같은 집합에 속한 노드를 만나게 되면 NO 반환
- 끊어져있는 그래프 고려 -> 모든 노드에서 DFS 탐색

2.시간복잡도
- O(V+E) = 20,000 + 200,000 = 220,000 (Worst case)
"""
import sys
sys.setrecursionlimit(10**6)

def DFS(start, visited, graph, group):
    visited[start] = group

    for v in graph[start]:
        if visited[v] == 0:
            res = DFS(v, visited, graph, -group)
            if not res:
                return False
        else:
            if visited[v] == group:
                return False
    return True

# 입력 받기
k = int(input())

for _ in range(k):
    # 입력 받기
    V, E = map(int, sys.stdin.readline().split())

    # 필요한 변수 생성 및 초기화
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    # 함수 실행
    for i in range(1, V+1):
        if visited[i] == 0:
            res = (DFS(i, visited, graph, 1))
            if not res:
                break

    print("YES") if res else print("NO")