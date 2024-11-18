"""
1.전략
- 비트마스크(Bit Mask)
- 집합 대신 2진수를 사용
- Shift 연산을 사용하여 명령어 구현 => 메모리 사용 최소화

2.시간 복잡도
- 시간 제한: 1.5초
- O(N) = 3,000,000
"""
import sys
input = sys.stdin.readline

# Input
M = int(input())

# Variables
S = 0b0

# Solution
for _ in range(M):
    cmd = input().rstrip().split()

    if len(cmd) == 1:
        if cmd[0] == "all":
            S = 0b111111111111111111111
        if cmd[0] == "empty":
            S = 0b0
        continue

    cmd, num = cmd[0], int(cmd[1])
    if cmd == "add":
        S |= (0b1 << num)
    if cmd == "remove":
        S &= ~(0b1 << num)
    if cmd == "check":
        if S & (0b1 << num):
            print(1)
        else:
            print(0)
    if cmd == "toggle":
        S ^= (0b1 << num) 