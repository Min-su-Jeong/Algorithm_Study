"""
1.전략
완전탐색
N의 범위 내 채널을 증가 or 감소시킴
버튼으로 누를 수 없는 채널인 경우 pass
누를 수 있는 채널인 경우, 대수 비교(최솟값 찾기)
"result = min(100~N번까지 눌러야 하는 횟수, 가장 가까운 채널로 이동해서 + or - 누르는 횟수)"

2.시간복잡도
O(N * M) = 500,001 * 6 = 3,000,006
=> 2초 내 가능
"""

N = int(input()) # 수빈이가 이동하려고 하는 채널
M = int(input()) # 고장난 버튼의 개수
if M:            # 고장난 버튼이 있는 경우만 입력 받기
    broken = set(input().split())
else:
    broken = set()

MAX = 1000000       # 채널 - or + 을 고려한 범위(0~999,999)
result = abs(100-N) # 결과 변수

for channel in range(MAX+1): # 범위 내 완전 탐색
    for c in str(channel):   # Channel의 숫자를 하나씩 분할하여 검증
        if c in broken:      # 누를 수 없는 채널인 경우 break
            break
    else:
        # 최소 버튼 클릭 횟수 구하기
        result = min(result, len(str(channel)) + abs(channel-N))
        
print(result)