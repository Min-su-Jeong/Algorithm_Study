"""
1. 전략
- 브루트포스(Brute Force)
- N의 최대 크기(50)가 크지 않음. 여러 개의 for문 사용 가능하다고 판단됨.
- 2차원 리스트(board)를 만들어서 현재 위치 기준 오른쪽, 아래 Swap
- Swap한 이후, 행과 열 기준으로 사탕의 최대 개수 구하기
- 개수를 구한 후, 배열 원상 복구

2. 시간 복잡도
- 시간 제한: 1초
- O(N^4) = 50^4 = 6,250,000 (가능)
"""

import sys
input = sys.stdin.readline

# Input
N = int(input())
board = [list(map(str, input().rstrip())) for _ in range(N)]

# Solution
res = 0

def findMax(board: list):
    global res

    for i in range(N):
        # 행 탐색
        cntRow = 1
        for j in range(N-1):
            if board[i][j] == board[i][j+1]:
                cntRow += 1
                res = max(res, cntRow)
            else:
                cntRow = 1

        # 열 탐색
        cntCol = 1
        for j in range(N-1):
            if board[j][i] == board[j+1][i]:
                cntCol += 1
                res = max(res, cntCol)
            else:
                cntCol = 1

for i in range(N):
    for j in range(N-1):
        if board[i][j] != board[i][j+1]:
            # 오른쪽 Swap
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            # 최대 개수 구하기
            findMax(board)
            # 원복
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        if board[j][i] != board[j+1][i]:
            # 아래쪽 Swap
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
            # 최대 개수 구하기
            findMax(board)
            # 원복
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i]

# Output
print(res)