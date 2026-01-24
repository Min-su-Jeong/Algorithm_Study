"""
풀이 전략
- 정렬 필요
  - 도착 시간 오름차순, 검문 시간 오름차순
- 대기 시간 누적합
  - 소가 검문 받는 동안 기다리는 소가 있으면 대기 시간 뒤에 누적
  - 검문 받는 소가 없으면, 다음 소가 도착한 시간 + 검문 시간
"""

N = int(input())
Q = [list(map(int, input().split())) for _ in range(N)]

ret = 0
Q.sort(key=lambda x: (x[0], x[1]))

for a, b in Q:
    if a > ret:
        ret = a + b
    else:
        ret += b

print(ret)