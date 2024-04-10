"""
1.전략
브루트포스: 아래와 오른쪽만 계속해서 swap 진행
전체 보드에서 사랑의 최대 개수를 구한 뒤 원상복구
다음 step으로 넘어가 위의 방법을 동일하게 반복

2. 시간복잡도
O(N^4) = 50**4 = 6,250,000 => 가능
"""
import sys
input = sys.stdin.readline

result = 0
N = int(input())
candy = [list(input()) for _ in range(N)]

def checkMaxCandy():
    maxCandy = 1 
    for i in range(N):
        cntRow, cntCol = 1, 1
        for j in range(N-1):
            # 행 검사
            if candy[i][j] == candy[i][j+1]:
                cntRow += 1
                maxCandy = max(maxCandy, cntRow)
            else:
                cntRow = 1
                
            # 열 검사
            if candy[j][i] == candy[j+1][i]:
                cntCol += 1   
                maxCandy = max(maxCandy, cntCol)
            else:
                cntCol = 1

    return maxCandy

for i in range(N):
    for j in range(N-1):
        # 오른쪽 Swap
        if candy[i][j] != candy[i][j+1]:                            
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j] # Swap
            result = max(result, checkMaxCandy())                   # 사탕의 최대 개수 구하기
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j] # 되돌리기
        
        # 아래쪽 Swap
        if candy[j][i] != candy[j+1][i]:
            candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]  # Swap
            result = max(result, checkMaxCandy())                      # 사탕의 최대 개수 구하기
            candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]  # 다시 되돌리기

print(result)