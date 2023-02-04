import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
num = sorted([int(input()) for _ in range(n)])
    
print(round(sum(num) / n)) # 산술평균
print(num[n // 2]) # 중앙값

# 최빈값
cnt = Counter(num).most_common()
modes = []
for i in cnt:
    if cnt[0][1]== i[1]: # 최빈값의 빈도수와 동일하면
        modes.append(i[0]) # modes 리스트에 추가

if len(modes) > 1:  # 최빈값이 여러 개 일 때
    print(modes[1]) # 두 번째로 작은 값 출력
else:               # 아닌 경우
    print(modes[0]) # 단일 최빈값 출력

print(max(num) - min(num)) # 범위