import sys
input = sys.stdin.readline
n, m = map(int, input().split())
d = {}

for i in range(1, n+1):
    a = input().rstrip()
    d[i] = a
    d[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(d[int(quest)])
    else:
        print(d[quest])