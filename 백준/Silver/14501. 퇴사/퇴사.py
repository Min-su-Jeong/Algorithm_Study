"""
1.전략
- 다이나믹 프로그래밍(Dynamic Programming)
- 상담이 가능한지 여부부터 체크 => 날짜가 뒤로 갈수록 상담일이 퇴사일을 초과하는 경우가 많아짐
- 이에 따라, 리스트를 뒤에서부터 체크하며 가능 여부 조건 분기
- Case 1. i일 상담 X : dp[i+1] => 지난 상담까지의 이익
- Case 2. i일 상담 O : dp[t[i]+i] + p[i] => dp[i일 + i일에 시작할 상담에 필요한 일 수] + 이익

2.시간 복잡도
- 제한 시간: 2초
- O(N) = 15
"""
import sys
input = sys.stdin.readline

# Input
N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]

# Variables
dp = [0 for _ in range(N+1)]

for i in reversed(range(N)):
    # 상담 O: i일 기준 상담일이 퇴사일 전인 경우
    if i + schedule[i][0] <= N:
        dp[i] = max(dp[i+1], schedule[i][1] + dp[i+schedule[i][0]])
    
    # 상담 X: i일 기준 상담일이 퇴사일을 초과하는 경우
    else:
        dp[i] = dp[i+1]

print(dp[0])