"""
문제 이해
- 만렙: 300
- 구만렙: 275
- 뀨만렙: 250
- 구간 1 ~ 4 존재

풀이 구상
- if~else문으로 분기하여 출력
"""

N = int(input())
M = list(map(int, input().split()))

for i in range(N):
    if M[i] >= 300:
        print(1, end=' ')
    elif 275 <= M[i] < 300:
        print(2, end=' ')
    elif 250 <= M[i] < 275:
        print(3, end=' ')
    else:
        print(4, end=' ')