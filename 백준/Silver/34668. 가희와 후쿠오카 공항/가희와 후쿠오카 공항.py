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
- M의 개수에서 50명씩 나눈 몫
  - 나머지 O: +1
  - 나머지 X: 0
  -> 가희가 기다려야하는 횟수
"""

# Input
Q = int(input())
M = [int(input()) for _ in range(Q)]

# Function
def timeToInt(t: str):
    h, m = map(int, t.split(':'))
    return h * 60 + m

def intToTime(i: int):
    h = "00" + str(i // 60)
    m = "00" + str(i % 60)

    return h[-2:] + ":" + m[-2:]

# Logic
for m in M:
    start = timeToInt("06:06")
    cnt = m // 50
    start += cnt * 12

    ret = intToTime(start)

    print(ret)