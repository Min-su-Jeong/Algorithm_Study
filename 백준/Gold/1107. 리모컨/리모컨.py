"""
1. 전략
- 브루트포스(Brute Force)
- 채널이 아래에서부터 올라가는 경우, 위에서 내려가는 경우를 고려
- 현재 채널의 숫자를 str로 변환해서 고장난 버튼에 들어있는지 확인
- 현재 채널에 고장난 버튼이 속하지 않으면 버튼을 누르는 횟수 계산
- "최적해 = min(마지막 최솟 값, 숫자 버튼 클릭 수 + '+/-' 버튼 클릭 수)"

2. 시간 복잡도
- 시간 제한: 2초
- O(N*M) = 1,000,000 * 7 = 7,000,000
"""

import sys;
input = sys.stdin.readline

N = int(input())
M = int(input())
broken = list(input().split()) if M != 0 else []

MAX = 1000001
res = abs(100 - N)

for i in range(MAX):
    for j in str(i):
        if j in broken:
            break
    else:
        res = min(res, len(str(i)) + abs(i - N))

print(res)
