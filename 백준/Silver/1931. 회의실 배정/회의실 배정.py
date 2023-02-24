import sys

cnt = 1
meet = []
input = sys.stdin.readline
n = int(input())

for i in range(n):
    s, e = map(int, input().split())
    meet.append([s, e])

# 1. 시작시간 기준 오름차순 정렬 & 2. 종료시간 기준 오름차순 정렬
# 회의시간이 짧으면서 빠르게 시작되는 시간부터 정렬
meet.sort(key = lambda x: x[0])
meet.sort(key = lambda x: x[1])

end = meet[0][1]
for i in range(1, n):
    if end <= meet[i][0]:
        cnt += 1
        end = meet[i][1]

print(cnt)     