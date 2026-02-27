import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
it = map(int, input().split())

flag = True
prev = next(it)
for i in it:
    if prev >= i:
        flag = False
        break
    
    prev = i

if flag: print(1)
else: print(0)