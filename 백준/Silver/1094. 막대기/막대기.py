"""
1.전략
- 그리디(Greedy)
- 64cm 막대기를 절반씩 자르면서 몇 개의 잘라진 막대기가 있으면 Xcm의 길이를 만들 수 있을까에 대한 문제
- 예) 23 = 16 + 4 + 2 + 1 / 48 = 32 + 16 / 32 = 32

2.시간 복잡도
- 시간 제한: 2초
- O(1)
"""
import sys
input = sys.stdin.readline

# Input
X = int(input())

# Variables
stick = [64, 32, 16, 8, 4, 2, 1]
res = 0

# Solution
for i in range(len(stick)):
    if stick[i] <= X:
        res += 1
        X -= stick[i]

    if X == 0:
        break

# Output
print(res)