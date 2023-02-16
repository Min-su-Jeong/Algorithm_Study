import sys
input = sys.stdin.readline
n, m, b = map(int, input().split())
G, sol = [], [] # ground, Solution

for _ in range(n):
    G += (map(int, input().split())) # 1차원으로 저장

for h in range(min(G), max(G)+1): # 최소/최대 범위에서만 반복 수행
    t, inv = 0, b # 시간, 인벤토리
    for g in G:
        if g > h: # 목표 높이보다 좌표의 높이가 큰 경우: 블록 제거
            t += 2*(g-h)
            inv += g-h
        elif g < h: # 목표 높이보다 좌표의 높이가 작은 경우: 블록 쌓기
            t += h-g
            inv -= h-g
    
    if inv>=0:
        sol.append([t, h])
        
sol.sort(key=lambda x:(x[0],-x[1])) # 걸린시간 오름차순, 높이 내림차순
print(sol[0][0],sol[0][1])