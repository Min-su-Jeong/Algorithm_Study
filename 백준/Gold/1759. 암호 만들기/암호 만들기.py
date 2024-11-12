"""
1.전략
- 백트래킹(Back Tracking)
- 최소 조건: 모음 1 + 자음 2, 오름차순 정렬
- 오름차순 + 중복 X => DFS 구현
- 최소 조건을 가지치기로 설정

2.시간복잡도
- 시간 제한: 2초
- O(2^C) = 2 ^ 15 = 32,768
"""
import sys
input = sys.stdin.readline

# Input
L, C = map(int, input().split())
ch = list(input().rstrip().split())
ch.sort()

# Variables
arr = []

# Solution
def backTracking(curNum: int):
    global arr

    # 가지치기
    if len(arr) == L:
        # 각각 모음/자음 개수
        cnt1, cnt2 = 0, 0 
        for c in arr:
            if c in "aeiou":
                cnt1 += 1
            else:
                cnt2 += 1
        
        # 조건에 만족해야 출력
        if cnt1 >= 1 and cnt2 >= 2:
            print(''.join(arr))
            return

    # 순회 조건
    for i in range(curNum, C):
        arr.append(ch[i])
        backTracking(i+1)
        arr.pop()

# Main
backTracking(0)