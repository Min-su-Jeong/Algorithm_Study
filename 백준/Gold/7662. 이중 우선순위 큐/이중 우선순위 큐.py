# 최댓값, 최솟값을 빠르게 찾아내는 방법? => '힙' 자료구조 사용
import sys
import heapq # 최소힙만 지원 => 최대힙 구현을 위해 입력값 n에 -1을 곱하고 출력 시에는 -1을 다시 곱하도록 함
input = sys.stdin.readline

# 이미 제거된 정수에 대한 pop 함수
def pop(q): 
    while q and not v[q[0][1]]:
        heapq.heappop(q)

t = int(input())
for _ in range(t): # 입력받은 값만큼 테스트 수행
    k = int(input())          # Q에 적용할 연산의 개수
    v = [False] * k          # 정수 여부
    hmax, hmin = [], []
    
    for i in range(k):
        s, n = input().split()
        n = int(n)
        if s == 'I': # 입력 값이 'I n'인 경우
            heapq.heappush(hmin, (n, i))
            heapq.heappush(hmax, (-n, i))
            v[i] = True # 정수 생성
        else:
            if n == 1: # 입력 값이 'D 1'인 경우 => 최대 힙 제거
                pop(hmax)
                if hmax:
                    v[hmax[0][1]] = False
                    heapq.heappop(hmax)
            else: # 입력 값이 'D -1'인 경우 => 최소 힙 제거
                pop(hmin)
                if hmin:
                    v[hmin[0][1]] = False
                    heapq.heappop(hmin)
    
    # 연산이 끝난 후 제거 되지 못한 최대 힙 & 최소 힙 제거
    pop(hmin)
    pop(hmax)
    print(-hmax[0][0], hmin[0][0]) if hmin or hmax else print("EMPTY")