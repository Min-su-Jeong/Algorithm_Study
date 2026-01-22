"""
문제 이해
- 국회의원 후보: N명
- 주민: M명
- 다른 표를 사들여 1번 표가 가장 많아지는 순간을 찾는다. (최솟값)

풀이 전략
- 다솜이를 제외한 후보자 리스트를 따로 받기
- 후보자 리스트 중 MAX 값 > 다솜이 값인 경우: 다솜+1, 해당 후보자 -1
- 다솜이가 처음으로 가장 많은 득표수를 가질 때까지 반복
"""

# Input
N = int(input())
dasom = int(input())
M = [int(input()) for _ in range(N-1)]

# Variables
ret = 0

# Logic
if N == 1:
    pass
else:
    while dasom <= max(M):
        dasom += 1
        M[M.index(max(M))] -= 1
        ret += 1

# Output
print(ret)