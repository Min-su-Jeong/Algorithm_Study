import sys
import heapq
input = sys.stdin.readline

h = [] # 최대 힙 저장을 위한 리스트
for _ in range(int(input())): # 연산의 개수만큼 반복
    x = int(input())
    if x != 0: # 입력 값이 0이 아닌 경우
        heapq.heappush(h, -x)
    else: # 입력 값이 0인 경우
        print(0) if not h else print(-heapq.heappop(h)) # 배열이 비어있으면 0 출력 아니면 최대 값 출력