"""
1.전략
- 비트마스크(Bitmask)
- 세로크기가 1인 조각 : 1 / 가로크기가 1인 조각 : 0 으로 설정
- 행/열 방향으로 각각 조각의 합을 구함.
- 이어져 있는 것을 처리하기 위해 하나씩 자릿수를 늘려나가며 연산

2.시간복잡도
- O(2^(N*M)) = 2 ^ 16 = 65,536 (Worst case)
  => 2초 이내 가능
"""
import sys; input = sys.stdin.readline

def bitMask():
    global res
    
    for case in range(1 << (N*M)):
        total = 0
        
        # 행방향 탐색
        for i in range(N):
            rowSum = 0
            for j in range(M):
                idx = (i*M) + j
                if case & (1 << idx):
                    rowSum = rowSum*10 + paper[i][j]
                else:
                    total += rowSum
                    rowSum = 0
            total += rowSum

        # 열방향 탐색
        for j in range(M):
            colSum = 0
            for i in range(N):
                idx = (i*M) + j
                if not (case & (1 << idx)):
                    colSum = colSum*10 + paper[i][j]
                else:
                    total += colSum
                    colSum = 0
            total += colSum

        res = max(res, total)

# 세로, 가로
N, M = map(int, input().split())

# 종이조각
paper = [list(map(int, input().rstrip())) for _ in range(N)]

# 필요한 변수 초기화
res = -1

# 함수 실행
bitMask()

# 결과 출력
print(res)