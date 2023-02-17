import sys
input = sys.stdin.readline
n = int(input())
cnt = abs(100 - n) # 채널 100번부터 시작
m = int(input())

if n == 100:
    print(0)
    sys.exit(0)

if m: # 고장이 있을 경우에만 입력 받기
    btn = set(input().split())
else:
    btn = set()

for i in range(1000000): 
    # 각 숫자별 고장 확인 후, 고장 시 break
    for j in str(i):
        if j in btn:
            break

    # 최소 이동 비교
    else:
        cnt = min(cnt, len(str(i)) + abs(i - n))

print(cnt)