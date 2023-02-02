# * 다시 칠해야 하는 경우
# 맨 왼쪽 위 칸이 흰색인 경우 or 검은색인 경우

# * 행과 열의 인덱스 합계가
# - 짝수: 처음 색과 동일해야함
# - 홀수: 처음 색과 달라야함
n, m = map(int, input().split())
board = []
res = []

# 체스판 입력받기(행의 개수만큼)
for _ in range(n):
    board.append(input())
    
for i in range(n-7):
    for j in range(m-7):
        w_cnt = 0 # 흰색 그리기
        b_cnt = 0 # 검은색 그리기
        
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0: # 짝수인 경우
                    if board[a][b]== 'W': # W인 경우
                        b_cnt += 1 # B로 칠하는 개수
                    else:
                        w_cnt += 1 # W로 칠하는 개수

                else: # 홀수인 경우
                    if board[a][b]== 'W': # W인 경우
                        w_cnt += 1 # W로 칠하는 개수
                    else:
                        b_cnt += 1 # B로 칠하는 개수  
        
        res.append(w_cnt)
        res.append(b_cnt)
        
print(min(res))