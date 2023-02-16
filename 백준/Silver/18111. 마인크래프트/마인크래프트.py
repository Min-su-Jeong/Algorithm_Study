import sys
input = sys.stdin.readline

time, height = -1, -1
n, m, b = map(int, input().split())

G = [] # ground
for _ in range(n):
    G.extend(list(map(int, input().split()))) # 1차원으로 저장
G.sort() # 오름차순 정렬

for h in range(G[0], G[-1]+1): # 최소/최대 범위에서만 반복 수행
    t, inv = 0, b
    for g in G:
        if g > h: # 목표 높이보다 좌표의 높이가 큰 경우: 블록 제거
            t += 2*(g-h)
            inv += g-h
        else: # 목표 높이보다 좌표의 높이가 작은 경우: 블록 쌓기
            t += h-g
            inv -= h-g
    
    if inv < 0: # 블록이 더이상 없는 경우
        break
    
    if time == -1 or t <= time: # 여러 개의 답 중 땅의 높이가 가장 높은 것 찾기
        time, height = t, h
        
print(time, height)