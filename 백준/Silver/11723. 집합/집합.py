
"""
1.전략
- 비트마스크
- shift 연산을 사용하여 문제 해결
- 메모리를 효과적으로 해결하기 위한 방법

2. 시간 복잡도
- M(N) = 3,000,000 (Worst Case)
"""
import sys; input = sys.stdin.readline

M = int(input())
S = 0b0
for _ in range(M):
    commands = input().rstrip()

    try:
        cmd, x = commands.split()
        x = int(x)
        if cmd == "add":
            S  = S | (0b1 << x)

        elif cmd == "remove":
            S = S & ~(0b1 << x)

        elif cmd == "check":
            if (S & (0b1 << x)):
                print(1)
            else:
                print(0)
                
        elif cmd == "toggle":
            S = S ^ (0b1 << x)

    except:
        if commands == "all":
            S = 0b111111111111111111111
        elif commands == "empty":
            S = 0b0
