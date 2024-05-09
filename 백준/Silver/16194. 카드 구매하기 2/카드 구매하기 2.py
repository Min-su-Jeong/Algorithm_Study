"""
1.전략
- 다이나믹 프로그래밍(Dynamic programming)
- i: 구하고 싶은 카드의 장수
- j: i보다 작은 카드의 장수
- j와 미지수 x의 합이 i가 나와야하기 때문에 
- j + x = i 라는 식을 만족시켜야 함 => x = i - j (i > j)
- 11052번 : 카드 구매하기 문제에서 반대의 경우로 생각하기

2.시간복잡도
- O(N) = 10,000
  => 1초 이내 가능
"""
import sys; input = sys.stdin.readline

def DP():
    global dp, N
    
    for i in range(1, N+1):
        for j in range(1, i+1):
            dp[i] = min(dp[i], dp[i-j] + Pn[j])
            
    return dp[N]

# 입력 받기
N = int(input())
Pn = [0] + list(map(int, input().split()))

# 필요한 변수 선언 및 초기화
dp = [10000] * (N+1)
dp[0] = 0

# 함수 실행 및 결과 출력
print(DP())