import sys
input = sys.stdin.readline

# 입력받기(input)
n = int(input())
m = int(input())
s = input().rstrip()

# 변수 정의
cur, cnt, res = 0, 0, 0 # 현재 위치(인덱스) / 'IOI'의 개수 / 결과 변수

# 해결 방법
while cur < (m-1):            # 문자열 끝에 도달할 때 동안
    if s[cur:cur+3] == 'IOI': # 'IOI'인 경우
        cur += 2              # 'I'에서부터 시작하여 'IOI' 여부 재탐색(2칸 이동)
        cnt += 1
        if cnt == n:          # 원하는 Pn을 찾은 경우
            res += 1 
            cnt -= 1          # 다음 위치에 존재하는 Pn을 찾기 위해 cnt - 1을 해줌
    else:                     # 'IOI'가 아닌 경우
        cur += 1              # 1칸 이동
        cnt = 0               # cnt 초기화

# 결과 출력
print(res)