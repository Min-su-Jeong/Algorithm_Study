"""
1.전략
- DP(Dynamic Programming)
- 자리수가 1개인 경우: 0 ~ 9까지 한 번씩만 사용,
- 자리수가 2개인 경우: 숫자의 위에 있는 수와 왼쪽에 있는 수를 더한 값

2.시간복잡도
- O(N^2) = 1,000 ^ 2 = 1,000,000
  => 1초 이내 가능
"""
import sys; input = sys.stdin.readline

# 입력 받기
n = int(input())

# 변수 초기화
dp = [1] * 10

# 솔루션
for i in range(n-1):
    for j in range(1, 10):
        dp[j] += dp[j-1]

# 결과 출력
print(sum(dp) % 10007)