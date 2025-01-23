"""
1.전략
- 수학
- 분자와 분모의 규칙 찾기: 홀수/짝수 라인에 따라 규칙이 달라지는 것을 발견
  - 짝수 라인: 분모: 1씩 커짐 / 분자: 1씩 작아짐
  - 홀수 라인: 분모: 1씩 작아짐 / 분자: 1씩 커짐
- X의 입력 값이 몇 번째 라인에 있는지 알 수 있는 알고리즘 구현

2.시간 복잡도
- 시간 제한: 0.5초
- O(root(N))
"""
import sys
input = sys.stdin.readline

# Input
X = int(input())

# Variables
line = 1

# Solution
while line < X:
    X -= line
    line += 1

if line % 2 == 0:
    a = X
    b = line-X+1
else:
    a = line-X+1
    b = X

print(f'{a}/{b}')