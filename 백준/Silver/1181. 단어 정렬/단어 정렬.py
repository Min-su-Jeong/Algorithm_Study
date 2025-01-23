"""
1.전략
- 구현
- 중복 제거: set() 함수 사용
- 조건: list의 sort() 함수 사용

2.시간 복잡도
- 시간 제한: 2초
- 시간 복잡도: O(NlogN)
"""
import sys
input = sys.stdin.readline

# Input
N = int(input())
words = set(input().rstrip() for _ in range(N))

# Solution
words = list(words)
words.sort(key=lambda x: (len(x), x))

# Output
for w in words:
    print(w)