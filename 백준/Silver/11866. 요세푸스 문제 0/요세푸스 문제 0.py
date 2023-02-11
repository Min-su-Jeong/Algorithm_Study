import sys
from collections import deque

queue = deque()
res = []

n, k = map(int, sys.stdin.readline().split());

for i in range(1, n+1):
    queue.append(i)

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    res.append(queue.popleft())

print("<", end='')
print(', '.join(map(str,res)), end='')
print(">")