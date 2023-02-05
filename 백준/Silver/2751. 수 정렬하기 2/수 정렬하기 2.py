import sys
input = sys.stdin.readline
n = [int(input()) for i in range(int(input()))]
print(*sorted(n), sep='\n')