import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline

# dfs 탐색법
def dfs(start, depth):
    #해당 노드 방문 체크
    visited[start] = True

    # 해당 시작점을 기준으로 그래프 탐색
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth + 1)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (1 + N) # 방문 여부 리스트

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0  # 컴포넌트 그래프 개수 저장
for i in range(1, N + 1):
    if not visited[i]:   # 만약 i번째 노드 방문 X 이고
        if not graph[i]: # 만약 해당 정점이 연결된 그래프가 없다면
            count += 1   # count + 1
            visited[i] = True  # 방문 처리
        else:  # 연결된 그래프가 있는 경우
            dfs(i, 0)  # dfs 탐색
            count += 1  # count +1

print(count)