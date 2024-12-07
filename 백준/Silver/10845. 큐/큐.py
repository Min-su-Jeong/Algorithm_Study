"""
1.전략
- 큐(Queue)
- 큐의 기본구조 파악하기

2.시간 복잡도
- 시간 제한: 0.5초
- O(N) = 10,000
"""
import sys
input = sys.stdin.readline

# Input
N = int(input())

# Variables
queue = []

# Solution
for _ in range(N):
    cmd = input().split()
    
    if cmd[0] == "push":
        queue.append(cmd[1])

    elif cmd[0] == "pop":
        if len(queue):
            print(queue.pop(0))
        else:
            print(-1)

    elif cmd[0] == "size":
        print(len(queue))

    elif cmd[0] == "empty":
        if len(queue):
            print(0)
        else:
            print(1)

    elif cmd[0] == "front":
        if len(queue):
            print(queue[0])
        else:
            print(-1)

    elif cmd[0] == "back":
        if len(queue):
            print(queue[-1])
        else:
            print(-1)