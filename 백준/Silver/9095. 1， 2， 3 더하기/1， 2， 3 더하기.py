"""
1.전략
- 다이나믹 프로그래밍(dp)
- 1~7까지 직접 계산해보며 규칙 먼저 찾기
  "n4 = n1 + n2 + n3", "n5 = n2 + n3 + n4"
  => [n] = [n-3] + [n-2] + [n-1]

2.시간복잡도
N(N * M^2) = 테스트 케이스 수(T) * func() 호출 수 = T * (n-2)^2+1
=> 1초 내 가능
"""
def func(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 4
    else:
        return func(x-1) + func(x-2) + func(x-3) 

T = int(input())     # 테스트 케이스의 개수
for _ in range(T):
    n = int(input()) # 정수 n
    dp = [0] * n     # n개의 배열 만들기
    print(func(n))