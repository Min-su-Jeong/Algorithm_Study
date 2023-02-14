import sys

input, arr = sys.stdin.readline, []
for _ in range(int(input())):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[1], x[0]))

for i in arr:
    print(i[0], i[1])