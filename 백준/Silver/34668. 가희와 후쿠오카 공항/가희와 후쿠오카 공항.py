"""
문제 이해
- 1. 국제선 -> 국내선
- 2. 국내선 정차
- 3. 국내선 -> 국제선
- 4. 국제선 정차
- if 만차 시간 over, 운행 종료 / else 1번 수행 / 정원 50명
- 국제선 (정차 2분) <-이동 4분-> 국내선 (정차 2분)
- 첫차: 06:00, 막차: 00:00
- Q: 줄의 수
- M: 가희 앞에 M명의 기다리는 사람 수
- 결과: 가희가 타게 될 버스 출발 시간

풀이 전략
- 우선, 시간 처리: int로 계산 후 마지막에 string 처리
- 첫번째 국내선 출발 시간: 06:06, 다음 출발마다 12분 증가
- M에서 50명씩 나눈 몫 = 가희가 기다려야하는 횟수
- 기다려야 하는 횟수 * 12 = 결과 값
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def timeToInt(t: str):
    h, m = map(int, t.split(':'))
    return h * 60 + m

def intToTime(i: int):
    h = i // 60
    m = i % 60

    return f"{h:02d}:{m:02d}"

Q = int(input())
for _ in range(Q):
    M = int(input())

    base_time = timeToInt("06:06")
    
    k = M // 50
    departure = base_time + k * 12

    if departure >= 24 * 60:
        print(-1)
    else:
        print(intToTime(departure))