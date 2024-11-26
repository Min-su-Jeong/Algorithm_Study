"""
1.전략
- 큐(Queue)
- 큐에 대한 기본 명령어 구현

2.시간 복잡도
- 시간 제한: 0.5초
- O(N) = 10,000
"""
import sys
input = sys.stdin.readline
queue = []

for _ in range(int(input())):
    com = input().split()
    if com[0] == 'push':
        queue.append(com[1])
        
    elif com[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            del queue[0]
            
    elif com[0] == 'size':
        print(len(queue))
        
    elif com[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
            
    elif com[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    
    elif com[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])