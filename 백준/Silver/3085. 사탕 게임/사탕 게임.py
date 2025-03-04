import sys
input = sys.stdin.readline

# Input
N = int(input())
board = [list(map(str, input().rstrip())) for _ in range(N)]

# Variables
res = 0

# Solution
def findMax(board: list):
    global res

    for i in range(N):
        maxRow = 1
        for j in range(N-1):
            if board[i][j] == board[i][j+1]:
                maxRow += 1
                res = max(res, maxRow)
            else:
                maxRow = 1
                
        maxCol = 1
        for j in range(N-1):
            if board[j][i] == board[j+1][i]:
                maxCol += 1
                res = max(res, maxCol)
            else:
                maxCol = 1

def solution():
    for i in range(N):
        for j in range(N-1):
            if board[i][j] != board[i][j+1]:
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                findMax(board)
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

            if board[j][i] != board[j+1][i]:
                board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
                findMax(board)
                board[j][i], board[j+1][i] = board[j+1][i], board[j][i]

# Main
solution()

# Output
print(res)