import sys;
input = sys.stdin.readline
yut = ['D', 'C', 'B', 'A', 'E']
for _ in range(3):
    i = sum(list(map(int, input().split())))
    print(yut[i])