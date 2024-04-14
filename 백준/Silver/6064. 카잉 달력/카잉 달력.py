"""
1.전략
- 브루트 포스
- "1476번: 날짜 계산"과 유사한 문제
- 나머지가 0인 경우 찾기 문제
"year = M * p + x = N * q + y(p,q는 자연수, year는 구하고자 하는 수)"

2.시간복잡도
O(N) = 40,000 
=> +1씩 증가가 아닌 m만큼 증가하므로 O(M*N)만큼 걸리지 않음
=> 1초 내 가능
"""
def calYear(M: int, N: int, x: int, y: int):
    # x%N == y%N? x가 N으로 나누어 떨어진 경우, 나머지가 0이기 때문
    for year in range(x, M*N+1, M): #
        if (year-x)%M == 0 and (year-y)%N == 0: # 조건 식
            return year
    return -1
    

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    year = calYear(M, N, x, y)
    print(year)