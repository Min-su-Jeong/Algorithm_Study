"""
1.전략
- 수학
- 뒤에서부터 시작
- 1) 뒷 값이 앖 값보다 작은 경우 찾기 
- 2) i-1 인덱스 값이 j 인덱스보다 큰 경우 => Swap
- 3) 뒷 값에 해당하는 인덱스부터 마지막까지 내림차순 정렬

2.시간 복잡도
- 시간 제한: 1초
- O(N^2) = 10,000 * 10,000 = 100,000,000
"""
import sys
input = sys.stdin.readline

# Input
N = int(input())
S = list(map(int, input().split()))

# Solution
for i in range(N-1, 0, -1):
    if S[i-1] > S[i]:                       # 1) 뒷 값이 앖 값보다 작은 경우 찾기
        for j in range(N-1, 0, -1):
            if S[i-1] > S[j]:               # 2) i-1 인덱스 값이 j 인덱스보다 큰 경우
                S[i-1], S[j] = S[j], S[i-1] # 2) Swap
                S = S[:i] + sorted(S[i:], reverse=True) # 3) 뒷 값에 해당하는 인덱스부터 마지막까지 내림차순 정렬
                print(*S)
                exit()

# 마지막 순열인 경우
print(-1)