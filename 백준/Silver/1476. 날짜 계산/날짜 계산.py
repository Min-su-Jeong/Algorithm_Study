"""
1. 전략
- 브루트포스(Brute Force)
- "어떤 수가 범위를 넘어가는 경우에는 1이 된다" => MOD 사용
- 순차적으로 수를 늘려가며 조건에 해당하면 빠져나오는 식으로 구현
- 규칙: (15*e)+E = (28*s)+S = (19*m)+M, (e,s,m은 정수)

2. 시간 복잡도
- 시간 제한: 2초
- O(1) = O(LCM(15, 28, 19)) = 7980
"""

import sys
input = sys.stdin.readline

# Input
E, S, M = map(int, input().split())

# Solution
year = 1
while True:
    condition = (year-E) % 15 == 0 and (year-S) % 28 == 0 and (year-M) % 19 == 0
    if condition:
        break
    else:
        year += 1

# Output
print(year)