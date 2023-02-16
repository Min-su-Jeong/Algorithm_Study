import sys
input = sys.stdin.readline
for _ in range(int(input())):
    c0, c1 = 1, 0
    for i in range(int(input())):
        c0,c1 = c1, c0+c1 # 피보나치 식
    print(c0,c1)